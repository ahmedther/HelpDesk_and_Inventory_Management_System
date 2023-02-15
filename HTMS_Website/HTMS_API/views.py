from django.db.models import Q
from rest_framework.response import Response
from django.http import JsonResponse
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
    request_object.description += f"\nLast Modified By {request.user.get_full_name()} ({request.user.username}) On {date_now}. Modification: Status Changed to {status_value}\n"
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


@api_view(["GET"])
def get_users(request):
    search_query = request.GET.get("search_value")
    user_tech_obj = Technician.objects.filter(
        Q(user__id__icontains=search_query)
        | Q(user__username__icontains=search_query)
        | Q(user__first_name__icontains=search_query)
        | Q(user__last_name__icontains=search_query)
        | Q(pr_number__icontains=search_query)
    ).distinct()

    user_tech_data = {}
    for users in user_tech_obj:
        user_tech_data[users.user.username] = {
            "id": users.user.id,
            "username": users.user.username,
            "first_name": users.user.first_name,
            "last_name": users.user.last_name,
            "email": users.user.email,
            "department": users.department,
            "designation": users.designation,
            "pr_number": users.pr_number,
            "extension_number": users.extension_number,
            "mobile_number": users.mobile_number,
        }
    return JsonResponse(user_tech_data)
    # user_user_obj = User.objects.get(pk=user_tech_obj["user_id"])
    # print(user_user_obj)
    # # user_obj_serializer = UserSerializer(user_tech_obj, many=True)
    # json_data = json.dumps(user_tech_obj)
    # return HttpResponse(json_data, content_type="application/json")


@api_view(["GET"])
def get_tickets(request):
    search_ticket = request.GET.get("search_value")
    ticket_objects = Requests.objects.distinct().filter(
        Q(id__icontains=search_ticket)
        | Q(requester_name__icontains=search_ticket)
        | Q(request_status__icontains=search_ticket)
        | Q(request_priority__icontains=search_ticket)
        | Q(request_category__icontains=search_ticket)
        | Q(request_technician__username__icontains=search_ticket)
        | Q(subject__icontains=search_ticket)
        | Q(request_creation_date__icontains=search_ticket)
    )
    ticket_data = {}
    for tickets in ticket_objects:
        ticket_data[tickets.requester_name] = {
            "id": tickets.id,
            "requester_name": tickets.requester_name,
            "request_type": tickets.request_type,
            "request_status": tickets.request_status,
            "request_mode": tickets.request_mode,
            "request_priority": tickets.request_priority,
            "request_category": tickets.request_category,
            "subject": tickets.subject,
            "location": tickets.location,
        }
        try:
            ticket_data[tickets.requester_name][
                "request_technician_id"
            ] = tickets.request_technician.id
        except:
            ticket_data[tickets.requester_name]["request_technician_id"] = 0
    return JsonResponse(ticket_data)
