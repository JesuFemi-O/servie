from django.urls import path
from . import views


urlpatterns = [
    path('basic/', views.BasicMailAPI.as_view(), name='basic-mail')
]
