from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", Index.as_view(), name = "index" ),
    path("dashboard/", Dashboard.as_view(), name = "dashboard"),
    path("addItem/", AddItem.as_view(), name="addItem"),
    path("editItem/<int:pk>/", EditItem.as_view(), name="editItem"),
    path("deleteItem/<int:pk>/", DeleteItem.as_view(), name="deleteItem"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name = "inventory/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "inventory/logout.html"), name = "logout"),
]
