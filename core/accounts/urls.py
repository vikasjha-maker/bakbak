from django.contrib import admin
from django.urls import path,include
from accounts.views import ( LoginView ,LogoutView, InstaModelView, InstaDetailView, RegisterView)
from . import views 


urlpatterns = [
path("login/", LoginView.as_view(), name="login"),
path("logout/", LogoutView.as_view(), name="logout"),
path("InstaModelView/", InstaModelView.as_view(), name="InstaModelView"),
path("InstaDetailView/<int:pk>/", views.InstaDetailView.as_view(), name="InstaDetailView"),
path("RegisterView/",RegisterView.as_view(),name="RegisterView"),

]