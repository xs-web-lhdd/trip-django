import json

from django import http
from django.views.generic import FormView

from system.forms import SendSmsCodeForm
from system.models import Slider
from utils.response import ServerErrorJsonResponse, BadRequestJsonResponse


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


# def send_sms(request):
#     pass
#     # 1. 拿到手机号，判断是否为真实的手机号码
#
#     # 2. 生成验证码，并存储
#     # TODO 3. 调用短信的发送接口
#     # 4. 告诉用户验证码发送是否成功（会把验证码直接告诉用户）


class SmsCodeView(FormView):
    form_class = SendSmsCodeForm

    def form_valid(self, form):
        """ 表单已经通过验证 """
        data = form.send_sms_code()
        if data is not None:
            return http.JsonResponse(data, status=201)
        return ServerErrorJsonResponse()

    def form_invalid(self, form):
        """ 表单没有通过验证 """
        err_list = json.loads(form.errors.as_json())
        return BadRequestJsonResponse(err_list)
