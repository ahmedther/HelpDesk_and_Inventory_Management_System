from HTMS_App.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.hashers import make_password
from datetime import date, timedelta
from HTMS_App.sms_sender import SendSms
import random
import requests
import itertools
import time


class Support:
    def __init__(self):
        pass

    def post_to_database(self, request):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        technician, status, req_asin_time = self.get_technician_and_status(
            request, date_now
        )
        search_user_selection = request.POST.get("search_user_selection", -1)
        if int(search_user_selection) > 0:
            req_user = Technician.objects.get(
                user=User.objects.get(id=search_user_selection)
            )
        else:
            self.create_new_user(request)
            req_user = Technician.objects.get(
                pr_number=request.POST["requester_pr_number"]
            )

        new_serv_req = Requests(
            requester_name=req_user.user.get_full_name(),
            requester_pr_number=req_user.pr_number,
            requester_designation=req_user.designation,
            requester_department=req_user.department,
            requester_email=req_user.user.email,
            requester_extension=req_user.extension_number,
            requester_phone_number=req_user.mobile_number,
            request_type=request.POST["request_type"],
            request_status=status,
            request_mode=request.POST["request_mode"],
            request_priority=request.POST["request_priority"],
            request_category=request.POST["request_category"],
            request_technician=technician,
            subject=request.POST["subject"],
            description=request.POST["description"],
            request_creation_date=date_now,
            request_submitter=request.user,
            last_modified_by=request.user,
            last_modified_date=date_now,
            request_assigned_time=req_asin_time,
            location=request.POST["location"],
        )
        new_serv_req.save()
        # new_serv_req = Requests(
        # requester_name=request.POST["requester_name"],
        # requester_pr_number=request.POST["requester_pr_number"],
        # requester_designation=request.POST["requester_designation"],
        # requester_department=request.POST["requester_department"],
        # requester_email=request.POST["requester_email"],
        # requester_extension=request.POST["requester_extension"],
        # requester_phone_number=request.POST["requester_phone_number"],

    def create_new_user(self, request):
        name = request.POST.get("requester_name", "")
        if not name:
            first_name = request.POST.get("user_first_name", "")
            last_name = request.POST.get("user_last_name", "")
        else:
            first_name, *rest = name.split(" ")
            last_name = " ".join(rest)

        gender = request.POST.get("user_gender", "")
        pr_num = request.POST.get("requester_pr_number", "")
        email = request.POST.get("requester_email", "")
        department = request.POST.get("requester_department", "")
        designation = request.POST.get("requester_designation", "")
        mobile_number = request.POST.get("requester_phone_number", "")
        extension_number = request.POST.get("requester_extension", "")
        password = make_password(pr_num)

        user, created = User.objects.get_or_create(
            username=pr_num,
            defaults={
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
            },
        )

        if created:
            employe_data = Technician(
                user=User.objects.get(pk=user.id),
                department=department,
                designation=designation,
                pr_number=pr_num,
                gender=gender,
                mobile_number=mobile_number,
                extension_number=extension_number,
            )
            employe_data.save()

            facility_id = request.POST.get("user_facility", "")
            if facility_id:
                employe_data.facility.set(
                    [FacilityDropdown.objects.get(pk=request.POST["user_facility"])]
                )

            return {
                "error": "✅ Your Account Has Been Created Successfully!!! ✅. 📢 Your Username & Password is your PR Number. 📢"
            }
        else:
            return {
                "error": f"⚠️ Your Already Have An Account !!! ⚠️. 📢 Enter Your PR Number {pr_num} as Username & Password to Login. 📢"
            }

    # return technician, status, req_asin_time

    def user_update(self, request):
        req_user = Technician.objects.get(pr_number=request.POST["requester_pr_number"])
        req_user.designation = request.POST.get("requester_designation")
        req_user.user.email = request.POST.get("requester_email")
        req_user.extension_number = request.POST.get("requester_extension")
        req_user.mobile_number = request.POST.get("requester_phone_number")
        req_user.save()
        try:
            req_user.user.save()
        except:
            pass

    def send_edit_request_to_db(self, request):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_request_inci = Requests.objects.get(pk=request.POST["ticket_pk"])
        technician, status, req_asin_time = self.get_technician_and_status(
            request, date_now, update_request_inci
        )
        update_fields = {
            "requester_name": "requester_name",
            "requester_pr_number": "requester_pr_number",
            "requester_designation": "requester_designation",
            "requester_department": "requester_department",
            "requester_email": "requester_email",
            "requester_extension": "requester_extension",
            "requester_phone_number": "requester_phone_number",
            "request_type": "request_type",
            "request_mode": "request_mode",
            "request_priority": "request_priority",
            "request_category": "request_category",
            "subject": "subject",
            "description": "description",
            "location": "location",
        }
        update_values = {}
        for field, value in update_fields.items():
            try:
                setattr(update_request_inci, field, request.POST[value])
                if request.POST[value] != "" and field != "requester_pr_number":
                    update_values.update({field.split("_")[-1]: request.POST[value]})

            except KeyError:
                pass

        if update_request_inci.request_status != status:
            update_request_inci.request_status = status
            update_values.update({"Status": status})

        if update_request_inci.request_technician != technician:
            update_request_inci.request_technician = technician
            if (
                technician != None
                and update_request_inci.request_technician.id == technician.id
            ):
                update_values.update(
                    {
                        "Techinican": f"{technician.first_name} {technician.last_name} ({technician.username})"
                    }
                )

        update_request_inci.last_modified_by = request.user
        update_request_inci.last_modified_date = date_now
        update_request_inci.request_assigned_time = req_asin_time
        update_values_in_string = ""
        if update_values != {}:
            for key, value in update_values.items():
                update_values_in_string += (
                    f"\n✔️ {key.capitalize()} Changed To {value} "
                )
            update_request_inci.description += f"\nLast Modified By {request.user.get_full_name()} ({request.user.username}) On {date_now}. Modification: {update_values_in_string}.\n\n"

        update_request_inci.save()
        self.user_update(request)

    def incident_context(self, user_full_name, context):
        context["user_fullname"] = user_full_name
        context["new_inc_req_type"] = NewIncidentRequestType.objects.values()
        context["new_inc_status"] = NewIncidentStatus.objects.values()
        context["new_inc_mode"] = NewIncidentMode.objects.values()
        context["new_inc_priority"] = NewIncidentPriority.objects.values()
        context["new_inc_category"] = (
            NewIncidentCategory.objects.all().order_by("category_name").values()
        )
        technicians_group = Group.objects.get(name="Technicians")
        context["technician"] = technicians_group.user_set.all()
        context["locations_obj"] = Location.objects.values().order_by("location_floor")
        return context

    def display_all_data(request):
        ticket_objects = Requests.objects.all().order_by("-id")
        context = {
            "user_fullname": request.user.get_full_name(),
            "ticket_objects": ticket_objects,
            "header": "All Tickets",
            "link_active_status_all_tickets": "link--active",
        }
        return context

    def non_it_home_content(request):
        user_full_name = request.user.get_full_name()
        technician = Technician.objects.get(user=request.user)
        ticket_objects = Requests.objects.filter(
            requester_pr_number=technician.pr_number
        )
        context = {
            "user_fullname": user_full_name,
            "ticket_objects": ticket_objects,
            "header": f"All Requests By {user_full_name}",
            "link_active_status_all_tickets": "link--active",
            "non_it": True,
        }
        return context

    def search_ticket(request, non_it=False):
        search_ticket = ""
        user_full_name = request.user.get_full_name()

        context = {
            "user_fullname": user_full_name,
            "header": "Search Results",
        }
        search_ticket = request.GET.get("search_ticket")
        context["search_ticket"] = search_ticket
        context["page_href"] = f"search_ticket={search_ticket}"
        ticket_objects = Requests.objects.distinct().filter(
            Q(id__icontains=search_ticket)
            | Q(requester_name__icontains=search_ticket)
            | Q(request_status__icontains=search_ticket)
            | Q(request_priority__icontains=search_ticket)
            | Q(request_category__icontains=search_ticket)
            | Q(request_technician__username__icontains=search_ticket)
            | Q(subject__icontains=search_ticket)
            | Q(request_creation_date__icontains=search_ticket)
            | Q(location=search_ticket)
        )

        if non_it:
            technician = Technician.objects.get(user=request.user)
            ticket_objects = ticket_objects.filter(
                Q(requester_pr_number=technician.pr_number)
            )

        if not ticket_objects:
            context["error"] = ["No data found!!!", "Please refine your search."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_to_handle(request, non_it=False):
        tickets_to_handle = ""
        user_full_name = request.user.get_full_name()

        context = {
            "user_fullname": user_full_name,
            "header": "Tickets to handle",
            "link_active_status_tickets_to_handle": "link--active",
        }
        tickets_to_handle = request.GET.get("tickets_to_handle")
        context["page_href"] = f"tickets_to_handle={tickets_to_handle}"

        if non_it:
            context["error"] = [
                f" {user_full_name} is not Authorised to View This Page. "
            ]
            return context, None

        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains=tickets_to_handle)
        )

        if not ticket_objects:
            context["error"] = ["No More Tickets To Handle."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def my_open_ticket(request, non_it=False):
        my_open_ticket = request.GET.get("my_open_ticket", "open")
        user_pk = request.user.id
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "My Open Tickets",
            "link_active_status_my_open_ticket": "link--active",
            "page_href": f"my_open_ticket={my_open_ticket}",
        }

        if non_it:
            technician = Technician.objects.get(user=request.user)
            ticket_objects = Requests.objects.distinct().filter(
                request_status__icontains=my_open_ticket,
                requester_pr_number=technician.pr_number,
            )
        else:
            ticket_objects = Requests.objects.distinct().filter(
                request_status__icontains=my_open_ticket, request_submitter__id=user_pk
            )
        if not ticket_objects:
            context["error"] = ["You don't have any Open Tickets."]
        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def my_tick_seven_days(request, non_it=False):
        my_tick_svn_days = request.GET.get("my_tick_svn_days")
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "My tickets in last 7 days",
            "link_active_status_my_tick_seven_days": "link--active",
            "page_href": f"my_tick_svn_days={my_tick_svn_days}",
        }

        today = datetime.now()
        svn_day = today - timedelta(days=7)
        if non_it:
            technician = Technician.objects.get(user=request.user)
            ticket_objects = Requests.objects.distinct().filter(
                requester_pr_number=technician.pr_number,
                request_creation_date__range=[svn_day, today],
            )
        else:
            ticket_objects = Requests.objects.distinct().filter(
                request_submitter__id=request.user.id,
                request_creation_date__range=[svn_day, today],
            )

        if not ticket_objects:
            context["error"] = ["You don't have any Tickets In Last Seven Days."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_open(request):
        tickets_open = ""
        user_full_name = request.user.get_full_name()

        context = {
            "user_fullname": user_full_name,
            "header": "Open Tickets",
            "link_active_status_tickets_open": "link--active",
        }
        tickets_open = request.GET.get("open")
        context["page_href"] = f"open={tickets_open}"
        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="open")
        )

        if not ticket_objects:
            context["error"] = ["No Open Tickets Left."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_assigned(self, request, non_it=False):
        tickets_assigned = request.GET.get("assigned")

        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Assigned Tickets",
            "link_active_status_assigned": "link--active",
            "page_href": f"assigned={tickets_assigned}",
        }

        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="assigned")
        )
        if non_it:
            ticket_objects = self.non_it_filter(ticket_objects, request)

        if not ticket_objects:
            context["error"] = ["No Assigned Tickets to Anyone."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_closed(self, request, non_it=False):
        tickets_closed = request.GET.get("closed")
        user_full_name = request.user.get_full_name()

        context = {
            "user_fullname": user_full_name,
            "header": "Closed Tickets",
            "link_active_status_closed": "link--active",
            "page_href": f"closed={tickets_closed}",
        }
        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="Closed")
        )
        if non_it:
            ticket_objects = self.non_it_filter(ticket_objects, request)

        if not ticket_objects:
            context["error"] = ["No Closed Tickets Found."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_on_hold(self, request, non_it=False):
        tickets_on_hold = request.GET.get("on_hold")
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "On Hold Tickets",
            "link_active_status_on_hold": "link--active",
            "page_href": f"on_hold={tickets_on_hold}",
        }

        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="On Hold")
        )
        if non_it:
            ticket_objects = self.non_it_filter(ticket_objects, request)

        if not ticket_objects:
            context["error"] = ["No Tickets On Hold."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def wait_for_feedback(self, request, non_it=False):
        wait_for_fback = request.GET.get("wait_for_fback")
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Waiting For Feedback",
            "link_active_status_wait_for_fback": "link--active",
            "page_href": f"wait_for_fback={wait_for_fback}",
        }

        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="Waiting for user feedback")
        )

        if non_it:
            ticket_objects = self.non_it_filter(ticket_objects, request)

        if not ticket_objects:
            context["error"] = ["No Waiting For Feedback Tickets Found!!!."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def tickets_resolved(self, request, non_it=False):
        tick_resolved = request.GET.get("resolved")

        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Resolved Tickets",
            "link_active_status_resolved": "link--active",
            "page_href": f"resolved={tick_resolved}",
        }

        ticket_objects = Requests.objects.distinct().filter(
            Q(request_status__icontains="Resolved")
        )

        if non_it:
            ticket_objects = self.non_it_filter(ticket_objects, request)

        if not ticket_objects:
            context["error"] = ["No Resolved Tickets Found!!!."]

        else:
            context["ticket_objects"] = ticket_objects

        return context, ticket_objects

    def paginator(request, context, paginate_name="ticket_objects"):
        page = request.GET.get("page")
        # results = 14
        results = 16
        paginator = Paginator(context[paginate_name], results)
        # context["paginator"] = paginator

        if not page:
            page = 1
        left_index = int(page) - 4
        if left_index < 1:
            left_index = 1

        right_index = int(page) + 5
        if right_index > paginator.num_pages:
            right_index = paginator.num_pages + 1

        custom_page_range = range(left_index, right_index)
        context["custom_page_range"] = custom_page_range
        try:
            context[paginate_name] = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            context[paginate_name] = paginator.page(page)
        except EmptyPage:
            page = paginator.num_pages
            context[paginate_name] = paginator.page(page)

        return context

    def humanize_datetime(self, time_in_seconds):
        time = timedelta(seconds=time_in_seconds)
        days = time.days
        hours, remainder = divmod(time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_in_between = {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
        return time_in_between

    def calculate_time_in_between(self, recent_time, earlier_time):
        try:
            recent_time = recent_time.replace(microsecond=0)
        except:
            return None
        try:
            earlier_time = earlier_time.replace(microsecond=0)
        except:
            return None
        if recent_time == earlier_time:
            return {"seconds": 0}
        try:
            between_time = recent_time - earlier_time
        except:
            return None
        if between_time:
            between_time = self.humanize_datetime(between_time.total_seconds())
        return between_time

    def update_ticket(self, request, pk):
        ticket_edit_objects = Requests.objects.get(pk=pk)
        context = {
            "ticket_edit_objects": ticket_edit_objects,
            "incident_header": f"Update Ticket #{pk}",
        }
        context["submit_type"] = context["incident_header"]
        context = self.incident_context(request.user.get_full_name(), context)
        if ticket_edit_objects.request_assigned_time:
            time_between_assign = self.calculate_time_in_between(
                ticket_edit_objects.request_assigned_time,
                ticket_edit_objects.request_creation_date,
            )
            context["time_between_assign"] = time_between_assign
        if ticket_edit_objects.request_resolved_time:
            time_between_resolve = self.calculate_time_in_between(
                ticket_edit_objects.request_resolved_time,
                ticket_edit_objects.request_assigned_time,
            )
            context["time_between_resolve"] = time_between_resolve
        if ticket_edit_objects.request_closed_time:
            time_between_close = self.calculate_time_in_between(
                ticket_edit_objects.request_closed_time,
                ticket_edit_objects.request_assigned_time,
            )
            context["time_between_close"] = time_between_close
        if ticket_edit_objects.request_closed_time:
            total_tat_time = self.calculate_time_in_between(
                ticket_edit_objects.request_closed_time,
                ticket_edit_objects.request_creation_date,
            )
            context["total_tat_time"] = total_tat_time

        return context

    def get_technician_and_status(self, request, date_now, ticket_edit_objects=None):
        try:
            technician = User.objects.get(pk=request.POST["request_technician"])
        except:
            technician = None
            req_asin_time = None
            status = "Open"
        if technician != None:
            if not ticket_edit_objects:
                status = "Assigned"
            else:
                status = ticket_edit_objects.request_status
            get_num = Technician.objects.get(user_id=technician.id)
            req_asin_time = date_now
            SendSms(number=get_num.mobile_number)

        return technician, status, req_asin_time

    def non_it_filter(self, ticket_objects, request):
        technician = Technician.objects.get(user=request.user)
        ticket_objects = ticket_objects.filter(requester_pr_number=technician.pr_number)
        return ticket_objects

    def get_assets_creation_context(self, request):
        context = {
            "user_fullname": request.user.get_full_name(),
            "link_active_status_create_new_asset": "link--active",
            "asset_header": "Create A New Asset",
            "create_assest": True,
        }
        return context

    def create_new_asset_type(self, request):
        try:
            image_url_api = self.get_categories(request.POST.get("asset_name"), 1)
            image_url_api = image_url_api["icons"][0]["raster_sizes"][-1]["formats"][
                -1
            ]["preview_url"]
        except:
            num = random.randint(1, 15)

            image_url_api = f"http://127.0.0.1:8000/static/HTMS_App/asset{num}.png"

        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_asset = Assets(
            asset_name=request.POST.get("asset_name").title(),
            asset_type=request.POST.get("asset_type"),
            asset_description=request.POST.get("description"),
            asset_creation_date=date_now,
            asset_creator=User.objects.get(id=request.user.id),
            image_url=image_url_api,
        )
        try:
            new_asset.save()
        except Exception as e:
            pass

    def get_categories(self, search_key, number_of_res):
        BASE_ENDPOINT = "https://api.iconfinder.com/v4/"
        API_SECRET = "NlhtuuCDXDjWp02MEBMqmWLzXus7jYVxicyPoISuo7aT3BvZJaKXyVO7ecvRuEmu"  # Keep this secret
        url = f"https://api.iconfinder.com/v4/icons/search?query={search_key}&count={number_of_res}"
        # Create the categories endpoint
        categories_endpoint = BASE_ENDPOINT + "categories"

        # Create the authorization header (and any additional ones if needed)
        headers = {"Authorization": "Bearer " + API_SECRET}

        # Make the GET request.
        response = requests.get(url, headers=headers)

        return response.json()

    def get_asset_head_objects(self, context):
        all_assets_heads = Assets.objects.all().order_by("asset_name").values()
        context["all_assets_heads"] = all_assets_heads
        return context

    def get_inventory_home_context(self, request):
        # random_number = random.randint(1, 15)
        asset_objects = AssetDetails.objects.all().order_by("-id")
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Assets Summary",
            "link_active_status_all_assests": "link--active",
            # "random_number": random_number,
            "asset_objects": asset_objects,
        }
        context = self.get_asset_head_objects(context)

        return context

    def add_quantity_to_asset(self, request):
        facilities = FacilityDropdown.objects.all().order_by("facility_name").values()
        asset_status = AssetStatus.objects.all().order_by("status_name").values()
        context = {
            "asset_header": "Add Quantity To An Asset",
            "add_quantity": True,
            "facilities": facilities,
            "asset_status": asset_status,
        }
        context = self.incident_context(request.user.get_full_name(), context)
        context = self.get_asset_head_objects(context)
        return context

    def user_creation_or_updation(self, request):
        search_user_selection = request.POST.get("search_user_selection", -1)
        pr_num = request.POST.get("requester_pr_number")

        if int(search_user_selection) > 0:
            user = User.objects.get(pk=search_user_selection)
            return user

        if int(search_user_selection) == 0 or pr_num:
            name = request.POST.get("requester_name", "")
            first_name, *rest = name.split(" ")
            last_name = " ".join(rest)
            password = make_password(pr_num)
            user, created = User.objects.get_or_create(
                username=pr_num,
                defaults={
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": request.POST.get("requester_email"),
                },
            )

            if created:
                user = User.objects.get(pk=user.id)
                employe_data = Technician(
                    user=user,
                    department=request.POST.get("requester_department"),
                    designation=request.POST.get("requester_designation"),
                    pr_number=pr_num,
                    mobile_number=request.POST.get("requester_phone_number")[:10],
                    extension_number=request.POST.get("requester_extension")[:10],
                )
                employe_data.save()

            return user

    def search_ticket_or_create(self, request, user):
        search_ticket_selection = request.POST.get("search_ticket_selection", -1)
        req_type = request.POST.get("request_type")
        if int(search_ticket_selection) > 0:
            search_ticket_obj = Requests.objects.get(pk=search_ticket_selection)
            return search_ticket_obj

        if int(search_ticket_selection) == 0 or req_type:
            date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            technician, status, req_asin_time = self.get_technician_and_status(
                request, date_now
            )

            new_serv_req = Requests(
                requester_name=f"{user.first_name} {user.last_name}",
                requester_pr_number=user.technician.pr_number,
                requester_designation=user.technician.designation,
                requester_department=user.technician.department,
                requester_email=user.email,
                requester_extension=user.technician.extension_number,
                requester_phone_number=user.technician.mobile_number,
                request_type=req_type,
                request_status=status,
                request_mode=request.POST["request_mode"],
                request_priority=request.POST["request_priority"],
                request_category=request.POST["request_category"],
                request_technician=technician,
                subject=request.POST["subject"],
                description=request.POST["description"],
                request_creation_date=date_now,
                request_submitter=request.user,
                last_modified_by=request.user,
                last_modified_date=date_now,
                request_assigned_time=req_asin_time,
                location=request.POST["location"],
            )
            new_serv_req.save()
            return new_serv_req

    def post_assest_quantity_addition(self, request):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        asset_detail = AssetDetails(
            asset_name=Assets.objects.get(pk=request.POST.get("add_asset_name")),
            brand=request.POST.get("asset_brand"),
            model_name=request.POST.get("model_name"),
            model_number=request.POST.get("model_number"),
            serial_number=request.POST.get("serial_number"),
            date_of_purchase=datetime.strptime(
                request.POST.get("date_of_purchase"), r"%Y-%m-%d"
            ),
            date_added=date_now,
            current_status=request.POST.get("asset_current_status"),
            description=request.POST.get("description"),
            facility=FacilityDropdown.objects.get(
                pk=request.POST.get("asset_facility")
            ),
        )
        user = self.user_creation_or_updation(request)
        if user:
            asset_detail.asset_user = user

            ticket_req_obj = self.search_ticket_or_create(request, user)
            asset_detail.assign_to_ticket = Requests.objects.get(pk=ticket_req_obj.id)
        asset_detail.save()

    def update_asset(self, request, pk):
        context = self.add_quantity_to_asset(request)
        asset_details_objects = AssetDetails.objects.get(pk=pk)
        context["asset_details_objects"] = asset_details_objects
        context[
            "asset_header"
        ] = f"Update Asset #{pk} {asset_details_objects.brand} - {asset_details_objects.asset_name.asset_name}"
        return context

    def send_edit_request_to_db_asset(self, request):
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_instance = User.objects.filter(pk=request.user.id).first()
        facility_instance = FacilityDropdown.objects.filter(
            id=request.POST.get("asset_facility")
        ).first()

        update_asset_details = AssetDetails.objects.get(
            pk=request.POST["asset_detail_pk"]
        )
        update_fields = {
            "brand": "asset_brand",
            "model_name": "model_name",
            "model_number": "model_number",
            "serial_number": "serial_number",
            "date_of_purchase": "date_of_purchase",
            "current_status": "asset_current_status",
            "facility": facility_instance,
            "description": "description",
        }
        update_values = {}

        for field, value in update_fields.items():
            try:
                if field == "facility":
                    if update_asset_details.facility != value:
                        setattr(update_asset_details, field, value)
                        update_values.update({field: value})

                if field == "description":
                    setattr(update_asset_details, field, request.POST[value])

                if field == "current_status":
                    if update_asset_details.current_status != request.POST[value]:
                        setattr(update_asset_details, field, request.POST[value])
                        update_values.update({field: request.POST[value]})
                else:
                    if request.POST[value] == "":
                        pass
                    else:
                        setattr(update_asset_details, field, request.POST[value])
                        update_values.update({field: request.POST[value]})

            except KeyError:
                pass

        update_asset_details.last_modified_by = user_instance
        update_asset_details.last_modified_date = date_now
        user = self.user_creation_or_updation(request)
        if user:
            update_asset_details.asset_user = user
            update_values.update(
                {"User Changed To ": f"{user.get_full_name()} ({user.username})"}
            )

            ticket_req_obj = self.search_ticket_or_create(request, user)
            if ticket_req_obj:
                update_asset_details.assign_to_ticket = Requests.objects.get(
                    pk=ticket_req_obj.id
                )
                {"Ticket Assigned To ": f"{user.get_full_name()} ({user.username})"}
        update_values_in_string = ""
        if update_values != {}:
            for key, value in update_values.items():
                update_values_in_string += (
                    f"\n✔️ {key.capitalize()} Changed To {value} "
                )
        update_asset_details.description += f"\nLast Modified By {request.user.get_full_name()} ({request.user.username}) On {date_now}. Modification: {update_values_in_string}.\n\n"

        update_asset_details.save()

    def search_assets(self, request):
        search_asset = ""   
        context = {
            "user_fullname": request.user.get_full_name(),
            "header": "Search Results",
        }
        search_asset = request.GET.get("search_asset")
        context["search_asset"] = search_asset
        context["page_href"] = f"search_asset={search_asset}"
        context = self.get_asset_head_objects(context)
        if search_asset.isdigit():
            search_with_id = int(search_asset)

        else:
            search_with_id = 0
        asset_objects = AssetDetails.objects.distinct().filter(
            Q(asset_name__asset_name__icontains=search_asset)
            | Q(brand__icontains=search_asset)
            | Q(model_name__icontains=search_asset)
            | Q(model_number__icontains=search_asset)
            | Q(serial_number__icontains=search_asset)
            | Q(date_of_purchase__icontains=search_asset)
            | Q(date_added__icontains=search_asset)
            | Q(current_status__icontains=search_asset)
            | Q(facility__facility_name__icontains=search_asset)
            | Q(asset_user__username__icontains=search_asset)
            | Q(asset_user__first_name__icontains=search_asset)
            | Q(asset_user__last_name__icontains=search_asset)
            | Q(asset_user__technician__pr_number__icontains=search_asset)
            | Q(assign_to_ticket__id=search_with_id)
        )

        if not asset_objects:
            context["error"] = ["No data found!!!", "Please refine your search."]

        else:
            context["asset_objects"] = asset_objects

        return context, asset_objects

    def filter_by_asset_id(self, request):
        context = {
            "user_fullname": request.user.get_full_name(),
            "link_active_status": "link--active",
        }

        asset_id = request.GET.get("asset_id")
        context["page_href"] = f"asset_id={asset_id}"
        asset_objects = AssetDetails.objects.distinct().filter(asset_name__id=asset_id)
        context = self.get_asset_head_objects(context)
        if not asset_objects:
            context["error"] = ["No data found!!!", "Please refine your search."]

        else:
            context["asset_objects"] = asset_objects
            context["header"] = f"{asset_objects[0].asset_name}"
            context["active_link"] = f"{asset_objects[0].asset_name.asset_name}"
        return context, asset_objects
