from django import http
from system.models import Slider


# Create your views here.

def slider_list(request):
    """ 轮播图接口
    {
        "meta": {},
        "objects": []
    }
    """
    data = {
        'meta': {

        },
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            # 在数据库中 img_url 是 ImageField 类型,可以通过 .url 这个属性,获取图片在磁盘中的路径
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    return http.JsonResponse(data)
