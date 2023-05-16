from django.urls import path
from . import views
from . import task

urlpatterns = [
    path("", views.home, name="home"),
    path("home_non_it/", views.home_non_it, name="home_non_it"),
    path("home_techs/", views.home_techs, name="home_techs"),
    path("login/", views.login_page, name="login_page"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("new_incident/", views.new_incident, name="new_incident"),
    path("update_incident/<str:pk>/", views.update_incident, name="update_incident"),
    path("inventory/", views.inventory, name="inventory"),
    path("new_assets/", views.new_assets, name="new_assets"),
    path("update_asset/<str:pk>/", views.update_asset, name="update_asset"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("automated_techinicans_report/", task.automated_techinicans_report, name="automated_techinicans_report"),
]
