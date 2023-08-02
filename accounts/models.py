from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """ 用户模型 """
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=32, unique=True)

    class Meta:
        db_table = 'account_user'

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''

    def add_login_record(self, **kwargs):
        """ 保存登录历史 """
        self.login_records.create(**kwargs)
