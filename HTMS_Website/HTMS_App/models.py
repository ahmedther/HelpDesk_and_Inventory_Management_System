from django.db import models

from django.contrib.auth.models import User


class FacilityDropdown(models.Model):

    facility_name = models.CharField(max_length=255)
    facility_code = models.CharField(max_length=255)

    def __str__(self):
        return self.facility_name


class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    # facility = models.ForeignKey(FacilityDropdown, on_delete=models.CASCADE)
    facility = models.ManyToManyField(FacilityDropdown)
    pr_number = models.CharField(max_length=100, null=False)
    gender = models.CharField(
        max_length=6, choices=[("Male", "Male"), ("Female", "Female")]
    )
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    extension_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"


class Requests(models.Model):
    requester_name = models.CharField(max_length=100, null=True)
    requester_pr_number = models.CharField(max_length=100, null=True)
    requester_designation = models.CharField(max_length=100, null=True)
    requester_department = models.CharField(max_length=100, null=True)
    requester_email = models.CharField(max_length=100, null=True)
    requester_extension = models.CharField(max_length=100, null=True)
    requester_phone_number = models.CharField(max_length=100, null=True)
    request_type = models.CharField(max_length=100, null=True)
    request_status = models.CharField(max_length=100, null=True)
    request_mode = models.CharField(max_length=100, null=True)
    request_priority = models.CharField(max_length=100, null=True)
    request_category = models.CharField(max_length=100, null=True)
    request_technician = models.ForeignKey(
        User, null=True, related_name="assignee", on_delete=models.CASCADE
    )
    request_submitter = models.ForeignKey(
        User, null=True, related_name="creator", on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=99999999, null=True)
    request_creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    request_completion_date = models.DateTimeField(
        auto_now_add=False,
        null=True,
        blank=True,
    )
    last_modified_by = models.ForeignKey(
        User, null=True, related_name="updater", on_delete=models.CASCADE
    )
    last_modified_date = models.DateTimeField(
        auto_now_add=True,
    )
    request_assigned_time = models.DateTimeField(blank=True, null=True)
    request_resolved_time = models.DateTimeField(blank=True, null=True)
    request_closed_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.requester_name} - {self.subject} "

    class Meta:
        ordering = ["-id"]


class NewIncidentRequestType(models.Model):
    request_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.request_name


class NewIncidentMode(models.Model):
    mode_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.mode_name


class NewIncidentStatus(models.Model):
    status_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.status_name


class NewIncidentPriority(models.Model):
    priority_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.priority_name


class NewIncidentCategory(models.Model):
    category_name = models.CharField(max_length=100, null=True)
    subcategory_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.category_name} - {self.subcategory_name}"
