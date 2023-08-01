from django import http
from django.db.models import Q
from django.views.generic import ListView

from sight.models import Sight


# Create your views here.
class SightListView(ListView):
    """ 景点列表 """
    # 每页放5条数据
    paginate_by = 5

    def get_queryset(self):
        """ 重写查询方法 """
        query = Q(is_valid=True)
        # 1. 热门景点
        is_hot = self.request.GET.get('is_hot', None)
        if is_hot:
            query = query & Q(is_hot=True)
        # 2. 精选景点
        is_top = self.request.GET.get('is_top', None)
        if is_top:
            query = query & Q(is_top=True)
        # 3. 景点名称搜索
        name = self.request.GET.get('name', None)
        if name:
            query = query & Q(name__icontains=name)
        queryset = Sight.objects.filter(query)
        return queryset

    def get_paginate_by(self, queryset):
        """ 从前端控制每一页的分页大小 """
        page_size = self.request.GET.get('limit', None)
        return page_size or self.paginate_by

    def render_to_response(self, context, **response_kwargs):
        """ ListView 的 render_to_response 返回的是 HTML, 所以进行重写返回 json """
        page_obj = context['page_obj']
        # if page_obj is not None:
        #     data = serializers.SightListSerializer(page_obj).to_dict()
        #     return http.JsonResponse(data)
        # else:
        #     return NotFoundJsonResponse()
        data = {
            'meta': {
                'total_count': page_obj.paginator.count,
                'page_count': page_obj.paginator.num_pages,
                'current_page': page_obj.number,
            },
            'objects': []
        }
        for item in page_obj.object_list:
            data['objects'].append({
                'id': item.id,
                'name': item.name,
                'main_img': item.main_img.url,
                'score': item.score,
                'province': item.province,
                'min_price': item.min_price,
                'city': item.city,
                # TODO 评论数量暂时无法获取
                'comment_count': 0
            })
        return http.JsonResponse(data)
