from django.db import models

from django.contrib.auth.models import User


class FacilityDropdown(models.Model):
    facility_name = models.CharField(max_length=255, db_index=True)
    facility_code = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.facility_name


class Technician(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="technician"
    )
    department = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    designation = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    # facility = models.ForeignKey(FacilityDropdown, on_delete=models.SET_NULL)
    facility = models.ManyToManyField(FacilityDropdown, blank=True, db_index=True)
    pr_number = models.CharField(max_length=100, null=False, db_index=True)
    gender = models.CharField(
        max_length=6, choices=[("Male", "Male"), ("Female", "Female")], blank=True
    )
    mobile_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        db_index=True,
    )
    extension_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        db_index=True,
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"


class Requests(models.Model):
    requester_name = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_pr_number = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_designation = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_department = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_email = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_extension = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    requester_phone_number = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_type = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_status = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_mode = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_priority = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_category = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    request_technician = models.ForeignKey(
        User, null=True, related_name="assignee", on_delete=models.SET_NULL, blank=True
    )
    request_submitter = models.ForeignKey(
        User, null=True, related_name="creator", on_delete=models.SET_NULL, blank=True
    )
    subject = models.CharField(max_length=100, null=True, db_index=True, blank=True)
    description = models.TextField(
        max_length=99999999, null=True, db_index=True, blank=True
    )
    request_creation_date = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True
    )
    # request_completion_date = models.DateTimeField(
    #     auto_now_add=False,
    #     null=True,
    #     blank=True,
    #     db_index=True,
    # )
    last_modified_by = models.ForeignKey(
        User,
        null=True,
        related_name="updater",
        on_delete=models.SET_NULL,
        blank=True,
    )
    last_modified_date = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True, null=True
    )
    request_assigned_time = models.DateTimeField(blank=True, null=True, db_index=True)
    request_resolved_time = models.DateTimeField(blank=True, null=True, db_index=True)
    request_closed_time = models.DateTimeField(blank=True, null=True, db_index=True)
    request_closed_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="request_closed_user",
        on_delete=models.SET_NULL,
    )
    location = models.CharField(max_length=100, null=True, db_index=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.requester_name} - {self.subject} "

    class Meta:
        ordering = ["-id"]


class NewIncidentRequestType(models.Model):
    request_name = models.CharField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.request_name


class NewIncidentMode(models.Model):
    mode_name = models.CharField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.mode_name


class NewIncidentStatus(models.Model):
    status_name = models.CharField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.status_name


class NewIncidentPriority(models.Model):
    priority_name = models.CharField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return self.priority_name


class NewIncidentCategory(models.Model):
    category_name = models.CharField(max_length=100, null=True, db_index=True)
    subcategory_name = models.CharField(max_length=100, null=True, db_index=True)

    def __str__(self):
        return f"{self.category_name} - {self.subcategory_name}"


class Location(models.Model):
    location_name = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    location_floor = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )

    def __str__(self):
        return f"{self.location_floor} - {self.location_name}"


class AssetStatus(models.Model):
    status_name = models.CharField(max_length=50, null=False, db_index=True)

    def __str__(self):
        return self.status_name


class Assets(models.Model):
    asset_name = models.CharField(
        max_length=100, null=False, unique=True, db_index=True, blank=True
    )
    asset_creation_date = models.DateTimeField(
        auto_now_add=True, db_index=True, blank=True
    )
    asset_type = models.CharField(max_length=100, null=True, db_index=True, blank=True)
    asset_description = models.TextField(
        max_length=99999999, null=True, db_index=True, blank=True
    )
    asset_creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="asset_creator",
        db_index=True,
        blank=True,
        null=True,
    )
    image_url = models.CharField(max_length=300, null=True, db_index=True)

    def __str__(self):
        return f"{self.asset_name} - {self.asset_type}"


class AssetDetails(models.Model):
    asset_name = models.ForeignKey(
        Assets,
        on_delete=models.SET_NULL,
        related_name="asset_details",
        db_index=True,
        blank=True,
        null=True
    )
    brand = models.CharField(max_length=100, null=True, db_index=True, blank=True)
    model_name = models.CharField(max_length=100, null=True, db_index=True, blank=True)
    model_number = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    serial_number = models.CharField(
        max_length=100, null=True, db_index=True, blank=True
    )
    date_of_purchase = models.DateTimeField(
        auto_now_add=False, db_index=True, blank=True, null=True
    )
    date_added = models.DateTimeField(auto_now_add=False, db_index=True, blank=True)
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="added_by",
        db_index=True,
        blank=True,
        null=True
    )
    expiration_date = models.DateTimeField(
        auto_now_add=False, db_index=True, blank=True, null=True
    )
    current_status = models.CharField(
        null=False, default="In Stock", db_index=True, blank=True, max_length=50
    )
    description = models.TextField(
        max_length=99999999,
        null=True,
        db_index=True,
        blank=True,
    )
    facility = models.ForeignKey(
        FacilityDropdown,
        on_delete=models.SET_NULL,
        related_name="facilities",
        db_index=True,
        blank=True,
        null=True,
    )
    asset_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="users",
        db_index=True,
        null=True,
        blank=True,
    )
    assign_to_ticket = models.ForeignKey(
        Requests,
        on_delete=models.SET_NULL,
        related_name="assign_to_ticket",
        db_index=True,
        null=True,
        blank=True,
    )
    last_modified_by = models.ForeignKey(
        User,
        null=True,
        related_name="last_modified_by",
        on_delete=models.SET_NULL,
        blank=True,
    )
    last_modified_date = models.DateTimeField(
        auto_now_add=True, db_index=True, null=True, blank=True
    )

    def __str__(self):
        return f"{self.id} - {self.asset_name.asset_name} - {self.brand} - {self.model_name} # {self.model_number} --- {self.serial_number}"
