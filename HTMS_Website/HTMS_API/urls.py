from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views

urlpatterns = [
    path("get_status/", views.get_status, name="get_status"),
    path("post_status/", csrf_exempt(views.post_status), name="post_status"),
    path(
        "post_reason_on_hold/",
        csrf_exempt(views.post_reason_on_hold),
        name="post_reason_on_hold",
    ),
]
