from rest_framework.response import Response
from rest_framework.decorators import api_view
from HTMS_App.models import *
from HTMS_API.serializers import *
from datetime import datetime


@api_view(["GET"])
def get_status(request):
    status_data = NewIncidentStatus.objects.all().order_by("id")
    status_data_serializer = NewIncidentStatSerializer(status_data, many=True)
    return Response(status_data_serializer.data)


@api_view(["POST"])
def post_status(request):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id = request.data["id"]
    status_value = request.data["status"]
    request_object = Requests.objects.get(pk=id)
    if status_value == "Resolved":
        request_object.request_resolved_time = date_now
    if status_value == "Closed":
        request_object.request_closed_time = date_now

    request_object.request_status = status_value
    request_object.save()
    request_object_serializer = RequestsSerializer(request_object)
    return Response(request_object_serializer.data)


@api_view(["POST"])
def post_reason_on_hold(request):
    user_full_name = request.user.get_full_name()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id = request.data["id"]
    desc_value = request.data["reson_for_hold"]
    request_object = Requests.objects.get(pk=id)
    request_object.description = f"{request_object.description} \n\nWas put On-Hold by {user_full_name} on {date_now}.\nReason : {desc_value}"
    request_object.save()
    request_object_serializer = RequestsSerializer(request_object)
    return Response(request_object_serializer.data)
