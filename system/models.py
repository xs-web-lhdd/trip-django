from django.db import models

from utils.models import CommonModel


# Create your models here.
class Slider(CommonModel):
    """ 轮播图 """
    name = models.CharField('名称', max_length=32)
    desc = models.CharField('描述', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('展现的位置', default=10)
    img = models.ImageField('图片地址', max_length=255, upload_to='%Y%m/slider')
    reorder = models.SmallIntegerField('排序字段', default=0, help_text="数字越大越靠前")
    start_time = models.DateTimeField('生效开始时间', null=True, blank=True)
    end_time = models.DateTimeField('生效结束的时间', null=True, blank=True)
    target_url = models.CharField('跳转的地址', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']

