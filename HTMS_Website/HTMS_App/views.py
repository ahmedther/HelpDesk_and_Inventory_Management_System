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
        context = sup.incident_context(request.user.get_full_name(), context={})
        context["incident_header"] = "New Incident"
        context["submit_type"] = "New Incident"
        if request.GET.get("non_it", False):
            context["non_it"] = True
            context["user_data"] = Technician.objects.get(user=request.user)
        if request.GET.get("techs", False):
            context["techs"] = True
            context["technician"] = context["technician"].filter(id=request.user.id)

        return render(request, "HTMS_App/new_incident.html", context)

    if request.method == "POST":
        context = sup.post_to_database(request)
        if context != None:
            return render(request, "HTMS_App/new_incident.html", context)
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
        print(request.POST)
        sup.send_edit_request_to_db(request)
        return redirect("home")


@login_required(login_url="login_page")
@allowed_users(allowed_group="Helpdesk")
def home(request):
    if request.method == "GET":
        sup = Support()
        filters = {
            "unresolved": sup.tickets_unresolved,
            "wait_for_fback": sup.wait_for_feedback,
            "on_hold": sup.tickets_on_hold,
            "closed": sup.tickets_closed,
            "assigned": sup.tickets_assigned,
            "open": Support.tickets_open,
            "my_tick_svn_days": Support.my_tick_seven_days,
            "my_open_ticket": Support.my_open_ticket,
            "tickets_to_handle": Support.tickets_to_handle,
            "search_ticket": Support.search_ticket,
            "reports_tat": Support.reports_tat,
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
        # from .task import automated_techinicans_report
        # automated_techinicans_report()
        return render(request, "HTMS_App/home.html", context)

    if request.method == "POST":
        check_tat_report = request.POST.get("tat_report")
        if check_tat_report:
            response = Support.get_tat_report(request)
            return response
        return render(request, "HTMS_App/home.html", context)


@login_required(login_url="login_page")
def home_non_it(request):
    if request.method == "GET":
        sup = Support()
        filters = {
            "unresolved": sup.tickets_unresolved,
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
@allowed_users(allowed_group="Technicians")
def home_techs(request):
    if request.method == "GET":
        sup = Support()
        filters = {
            "unresolved": sup.tickets_unresolved,
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
                context, ticket_objects = filter_func(request, techs=True)
                if not ticket_objects:
                    context["home_techs"] = True
                    return render(request, "HTMS_App/home.html", context)
                context = Support.paginator(request, context)
                context["home_techs"] = True
                return render(request, "HTMS_App/home.html", context)

        # If no filter is present in the request, display all data
        context = Support.techs_home_content(request)
        context = Support.paginator(request, context)
        context["home_techs"] = True
        return render(request, "HTMS_App/home.html", context)

    elif request.method == "POST":
        return render(request, "HTMS_App/home.html")

@login_required(login_url="login_page")
@allowed_users(allowed_group="Helpdesk")
def inventory(request):
    if request.method == "GET":
        sup = Support()
        filters = {
            "search_asset": sup.search_assets,
            "asset_id": sup.filter_by_asset_id,
        }
        for filter_name, filter_func in filters.items():
            if request.GET.get(filter_name):
                context, ticket_objects = filter_func(request)
                if not ticket_objects:
                    return render(request, "HTMS_App/inventory.html", context)
                context = Support.paginator(
                    request, context, paginate_name="asset_objects"
                )
                return render(request, "HTMS_App/inventory.html", context)
        context = sup.get_inventory_home_context(request)
        context = Support.paginator(request, context, paginate_name="asset_objects")
        return render(request, "HTMS_App/inventory.html", context)

    if request.method == "POST":
        return render(request, "HTMS_App/inventory.html", context)


@login_required(login_url="login_page")
@allowed_users(allowed_group="Inventory")
def new_assets(request):
    sup = Support()
    if request.method == "GET":
        filters = {
            "asset_creation": sup.get_assets_creation_context,
            "quantity_addition": sup.add_quantity_to_asset,
            "bulk_quantity_addition": sup.bulk_add_quantity,
            "bulk_asset_scrap": sup.bulk_asset_scrap,
        }

        for filter_name, filter_func in filters.items():
            if request.GET.get("arg") == filter_name:
                context = filter_func(request)
                return render(request, "HTMS_App/new_assets.html", context)

    if request.method == "POST":
        sup = Support()
        if request.POST.get("bulk_add_qty_asset") == "bulk_add_qty_asset":
            context = sup.post_bulk_assest_quantity_addition(request)
            if context:
                return render(request, "HTMS_App/new_assets.html", context)

        submit_type = {
            "create_asset": sup.create_new_asset_type,
            "add_qty_asset": sup.post_assest_quantity_addition,
            "bulk_asset_scrap": sup.post_bulk_asset_scrap,
        }

        for submit_name, submit_func in submit_type.items():
            if request.POST.get(submit_name):
                submit_func(request)
        return redirect("inventory")


@login_required(login_url="login_page")
def update_asset(request, pk):
    sup = Support()
    context = sup.update_asset(request, pk)
    if request.method == "GET":
        return render(request, "HTMS_App/new_assets.html", context)

    if request.method == "POST":
        sup.send_edit_request_to_db_asset(request)
        return redirect("inventory")
