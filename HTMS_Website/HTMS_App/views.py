from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# from django.http import HttpResponse, HttpResponsePermanentRedirect
# from django.db.models import Q


from HTMS_App.decorators import *
from HTMS_App.models import *
from HTMS_App.support import *


@check_auth_redirect
def sign_up(request):
    if request.method == "GET":
        facility = (
            FacilityDropdown.objects.all().exclude(facility_name="ALL").order_by("-id")
        )
        context = {"facility": facility}
        return render(request, "HTMS_App/sign_up.html", context)

    if request.method == "POST":
        sup = Support()
        context = sup.create_new_user(request)
        request.session["context"] = context
        return redirect("login_page")


@check_auth_redirect
def login_page(request):
    try:
        context = request.session["context"]
        request.session["context"] = None
    except:
        context = {}
    if request.method == "GET":
        return render(request, "HTMS_App/login_page.html", context)
    if request.method == "POST":

        # Login User
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            context[
                "error"
            ] = "Wrong User ID or Password. Try again or call 33333 /33330 to reset it."
            return render(request, "HTMS_App/login_page.html", context)
        if user:
            login(request, user)
            user_full_name = request.user.get_full_name()
            context = {"user_fullname": user_full_name}
            return redirect("home")


# @login_required(login_url="login_page")
# def index(request):

#     print(context)
#     if request.method == "GET":

#         return render(request, "HTMS_App/index.html", context)


@login_required(login_url="login_page")
def logout_user(request):
    logout(request)
    return redirect("login_page")


@login_required(login_url="login_page")
def new_incident(request):
    sup = Support()
    if request.method == "GET":
        context = {}
        context = sup.incident_context(request.user.get_full_name(), context)
        context["incident_header"] = "New Incident"
        context["submit_type"] = "New Incident"
        if request.GET.get("non_it", False):
            context["non_it"] = True
            context["user_data"] = Technician.objects.get(user=request.user)
        return render(request, "HTMS_App/new_incident.html", context)

    if request.method == "POST":
        sup.post_to_database(request)
        return redirect("home")


@login_required(login_url="login_page")
def update_incident(request, pk):
    sup = Support()
    context = sup.update_ticket(request, pk)
    if request.GET.get("non_it", False):
        context["non_it"] = True

    if request.method == "GET":

        return render(request, "HTMS_App/new_incident.html", context)

    if request.method == "POST":
        sup.send_edit_request_to_db(request)
        return redirect("home")


@login_required(login_url="login_page")
@allowed_users
def home(request):

    if request.method == "GET":
        sup = Support()
        filters = {
            "resolved": sup.tickets_resolved,
            "wait_for_fback": sup.wait_for_feedback,
            "on_hold": sup.tickets_on_hold,
            "closed": sup.tickets_closed,
            "assigned": sup.tickets_assigned,
            "open": Support.tickets_open,
            "my_tick_svn_days": Support.my_tick_seven_days,
            "my_open_ticket": Support.my_open_ticket,
            "tickets_to_handle": Support.tickets_to_handle,
            "search_ticket": Support.search_ticket,
        }

        for filter_name, filter_func in filters.items():
            if request.GET.get(filter_name):
                context, ticket_objects = filter_func(request)
                if not ticket_objects:
                    return render(request, "HTMS_App/home.html", context)
                context = Support.paginator(request, context)
                return render(request, "HTMS_App/home.html", context)

        # If no filter is present in the request, display all data
        context = Support.display_all_data(request)
        context = Support.paginator(request, context)
        return render(request, "HTMS_App/home.html", context)

    if request.method == "POST":
        return render(request, "HTMS_App/home.html", context)


@login_required(login_url="login_page")
def home_non_it(request):

    if request.method == "GET":

        sup = Support()
        filters = {
            "resolved": sup.tickets_resolved,
            "wait_for_fback": sup.wait_for_feedback,
            "on_hold": sup.tickets_on_hold,
            "closed": sup.tickets_closed,
            "assigned": sup.tickets_assigned,
            "open": Support.my_open_ticket,
            "my_tick_svn_days": Support.my_tick_seven_days,
            "my_open_ticket": Support.my_open_ticket,
            "tickets_to_handle": Support.tickets_to_handle,
            "search_ticket": Support.search_ticket,
        }

        for filter_name, filter_func in filters.items():
            if request.GET.get(filter_name):
                context, ticket_objects = filter_func(request, non_it=True)
                if not ticket_objects:
                    context["non_it"] = True
                    return render(request, "HTMS_App/home.html", context)
                context = Support.paginator(request, context)
                context["non_it"] = True
                return render(request, "HTMS_App/home.html", context)

        # If no filter is present in the request, display all data
        context = Support.non_it_home_content(request)
        context = Support.paginator(request, context)
        context["non_it"] = True
        return render(request, "HTMS_App/home.html", context)

    elif request.method == "POST":
        return render(request, "HTMS_App/home.html")


@login_required(login_url="login_page")
@allowed_users
def inventory(request):

    if request.method == "GET":
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Assets Summary",
            "link_active_status_all_assests": "link--active",
        }
        return render(request, "HTMS_App/inventory.html", context)

    if request.method == "POST":
        return render(request, "HTMS_App/inventory.html", context)


@login_required(login_url="login_page")
@allowed_users
def new_assets(request):
    sup = Support()
    if request.method == "GET":
        filters = {
            "asset_creation": sup.get_assets_creation_context,
        }

        for filter_name, filter_func in filters.items():
            if request.GET.get("arg") == filter_name:
                context = filter_func(request)
                return render(request, "HTMS_App/new_assets.html", context)

    if request.method == "POST":
        submit_type = {
            "create_asset": Support.create_new_asset_type,
        }

        for submit_name, submit_func in submit_type.items():
            if request.POST.get(submit_name):
                submit_func(request)

        return redirect("inventory")
