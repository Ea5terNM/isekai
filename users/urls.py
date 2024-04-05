from django.urls import path , include
from users import views



urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register",views.register, name="register"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("profile",views.profile, name="profile"),
    path("shopp",views.shopp, name="shopp"),
    # users/urls.py
]




