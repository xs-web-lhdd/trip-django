from django.urls import path

from system import views

urlpatterns = [
    # 轮播图数据接口
    path('slider/list/', views.slider_list, name="slider_list"),
]
