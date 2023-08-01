from django.db import models

from utils.models import CommonModel


# Create your models here.
class Sight(CommonModel):
    """ 景点基础信息 """
    name = models.CharField('名称', max_length=64)
    desc = models.CharField('描述', max_length=256)
    main_img = models.ImageField('主图', upload_to='%Y%m/sight/', max_length=256)
    banner_img = models.ImageField('详情主图', upload_to='%Y%m/sight/', max_length=256)
    content = models.TextField('详细')
    score = models.FloatField('评分', default=5)
    min_price = models.FloatField('最低价格', default=0)
    province = models.CharField('省份', max_length=32)
    city = models.CharField('市区', max_length=32)
    area = models.CharField('区/县', max_length=32, null=True)
    town = models.CharField('乡镇', max_length=32, null=True)

    is_top = models.BooleanField('是否为精选景点', default=False)
    is_hot = models.BooleanField('是否为热门景点', default=False)

    # images = GenericRelation(ImageRelated,
    #                          verbose_name='关联的图片',
    #                          related_query_name='rel_sight_iamges')

    class Meta:
        db_table = 'sight'
        ordering = ['-updated_at']

    @property
    def comment_count(self):
        """ 评论总数 """
        return self.comments.filter(is_valid=True).count()

    @property
    def image_count(self):
        """ 景点图片的数量 """
        return self.images.filter(is_valid=True).count()
