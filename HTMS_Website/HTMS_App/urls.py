from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home_non_it/", views.home_non_it, name="home_non_it"),
    path("login/", views.login_page, name="login_page"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("new_incident/", views.new_incident, name="new_incident"),
    path("update_incident/<str:pk>/", views.update_incident, name="update_incident"),
    path("inventory/", views.inventory, name="inventory"),
    path("new_assest/", views.new_assest, name="new_assest"),
    path("sign_up/", views.sign_up, name="sign_up"),
]
