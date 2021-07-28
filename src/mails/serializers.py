from rest_framework import serializers
from .senders import MailSender


class BasicMailSerializer(serializers.Serializer):
    email_subject = serializers.CharField(max_length=200)
    email_body = serializers.CharField()
    to_email = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    def send_mail(self, validated_data):
        MailSender.send_basic_email(validated_data)
        return
