from django.urls import path, include
from . import views

urlpatterns = [
    path('join', views.join, name="join"),
    path('host', views.host, name="host"),
    path('wallet', views.wallet, name="wallet"),
    path('hostsubmited', views.hostsData, name="hostsdata"),
]