from django.shortcuts import redirect, render
from django.contrib.auth.models import Group


def check_auth_redirect(login_page):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return login_page(request, *args, **kwargs)

    return wrapper_func


def allowed_users(view_func):
    def wrapper_func(request, *args, **kwargs):

        try:
            group = request.user.groups.get(name="Helpdesk")
            return view_func(request)
        except Group.DoesNotExist:
            return redirect("home_non_it")

    return wrapper_func
