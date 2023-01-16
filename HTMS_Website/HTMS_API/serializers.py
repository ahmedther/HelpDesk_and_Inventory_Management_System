from rest_framework import serializers
from HTMS_App.models import *


class NewIncidentStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewIncidentStatus
        fields = "__all__"


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = "__all__"
