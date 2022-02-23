from rest_framework import serializers

class SmsSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    sms = serializers.IntegerField()