from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from HTMS_App.models import *


class TechnicianInline(admin.StackedInline):
    model = Technician
    can_delete = False
    verbose_name_plural = "Technician"


admin.site.register(NewIncidentRequestType)
admin.site.register(NewIncidentMode)
admin.site.register(NewIncidentStatus)
admin.site.register(NewIncidentPriority)
admin.site.register(NewIncidentCategory)
admin.site.register(FacilityDropdown)
admin.site.register(Requests)
admin.site.register(AssetStatus)
admin.site.register(Assets)
admin.site.register(AssetDetails)
admin.site.register(Location)


# admin.site.register(FacilityDropdown)

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (TechnicianInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# CHnage admin Panel
admin.site.site_header = "Helpdesk Ticket Management System Admin Panel"
admin.site.site_title = "HTMS Admin Panel"
admin.site.index_title = "Helpdesk Ticket Management System Administration"
