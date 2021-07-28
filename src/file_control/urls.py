from django.urls.conf import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)

router.register('file-upload', views.GenericFileUploadView)

urlpatterns = [
    path('', include(router.urls))
]
