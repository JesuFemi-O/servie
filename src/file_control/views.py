from django.shortcuts import render
from .models import GenericFileUpload
from .serializers import GenericFileUploadSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class GenericFileUploadView(ModelViewSet):
    serializer_class = GenericFileUploadSerializer
    queryset = GenericFileUpload.objects.all()
