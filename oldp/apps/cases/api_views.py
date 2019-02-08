from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from oldp.api import SmallResultsSetPagination
from oldp.apps.cases.filters import CaseAPIFilter
from oldp.apps.cases.models import Case
from oldp.apps.cases.serializers import CaseSerializer, CASE_API_FIELDS


class CaseViewSet(viewsets.ModelViewSet):
    pagination_class = SmallResultsSetPagination  # limit page (other content field blows up response size)
    queryset = Case.get_queryset()
    serializer_class = CaseSerializer
    # lookup_field = 'slug'

    filter_backends = (OrderingFilter, DjangoFilterBackend, )
    filterset_class = CaseAPIFilter
    ordering_fields = ('date', )

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Case.get_queryset()\
            .select_related('court')\
            .only(*CASE_API_FIELDS)