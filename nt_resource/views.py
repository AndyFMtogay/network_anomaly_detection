from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from nt_resource.filters import CatNormalResourceFilter
from rest_framework import filters
from nt_core.pagination import RsPagination

from nt_core.exceptions import RsError

from nt_resource.models import CatNormalResource
from nt_resource.serializers import (
    CatNormalResourceListSerializer
)


class CatNormalResourceView(APIView):
    def get(self, request):
        req_data = request.GET
        _id = req_data.get('id')
        if not _id:
            raise RsError('id不可缺少')

        cat_normal_obj = CatNormalResource.objects.filter(
            id=_id
        ).first()
        if not cat_normal_obj:
            raise RsError('数据不存在')
        ser_data = CatNormalResourceListSerializer(cat_normal_obj).data
        return Response(ser_data)

    def put(self, request):
        req_data = request.data
        _id = req_data.get('id')
        if not _id:
            raise RsError('id不可缺少')

        cat_normal_obj = CatNormalResource.objects.filter(id=_id).first()
        if not cat_normal_obj:
            raise RsError("id不存在")

        ser = CatNormalResourceListSerializer(
            cat_normal_obj, req_data, partial=True
        )

        if ser.is_valid():
            ser.save()
        else:
            raise RsError(ser.errors)

        return Response({"result": True, "id": _id})

    def delete(self, request):
        req_data = request.data
        delete_ids = req_data.get('delete_ids')
        rows = CatNormalResource.objects.filter(
            id__in=delete_ids
        ).delete()
        return Response({"result": True, "rows": rows})


class CatNormalResourceListView(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                GenericViewSet):
    """
    搜索、过滤、排序
    """
    queryset = CatNormalResource.objects.all()
    serializer_class = CatNormalResourceListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filter_class = CatNormalResourceFilter
    pagination_class = RsPagination

    # 前端参数  search  如查找appid为1212开头的 search=1212
    search_fields = ('^appid',)

    # 前端参数 ordering  升序:create_time 降序:-create_time
    ordering_fields = ('create_time', 'update_time')

    def retrieve(self, request, *args, **kwargs):
        """
        获取单条记录的详情
        如：cat_normal_list/9e1fdbbf-f399-45f3-979a-c48d8bf4fae6
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
