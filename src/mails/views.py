from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, status
from rest_framework.response import Response
from mails.serializers import BasicMailSerializer
# Create your views here.


class BasicMailAPI(GenericAPIView):
    serializer_class = BasicMailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.send_mail(serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={"Error": "Unable to send Email"}, status=status.HTTP_400_BAD_REQUEST)
