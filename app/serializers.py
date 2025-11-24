from rest_framework import serializers
from app.models import ToDo
from django.conf import settings

class TodoSerializer(serializers.ModelSerializer):

    message = serializers.SerializerMethodField()

    class Meta:
        model=ToDo
        
        fields="__all__"

    def get_message(self, obj):
        return settings.MY_SECRET_MESSAGE