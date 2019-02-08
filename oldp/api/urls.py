from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from oldp.api.views import CourtViewSet, CityViewSet, StateViewSet, CountryViewSet, LawViewSet, LawBookViewSet
from oldp.apps.annotations.api_views import CaseAnnotationViewSet, AnnotationLabelViewSet
from oldp.apps.cases.api_views import CaseViewSet
from . import schema_view

router = routers.DefaultRouter()

router.register(r'laws', LawViewSet)
router.register(r'law_books', LawBookViewSet)

router.register(r'cases', CaseViewSet)

router.register(r'courts', CourtViewSet)
router.register(r'cities', CityViewSet)
router.register(r'states', StateViewSet)
router.register(r'countries', CountryViewSet)

router.register(r'annotation_labels', AnnotationLabelViewSet)
router.register(r'case_annotations', CaseAnnotationViewSet)

urlpatterns = [
    url(r'^schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^schema/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),

    url(r'^token-auth/', authtoken_views.obtain_auth_token),
    url(r'^', include(router.urls)),
]