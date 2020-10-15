# importing necessary files
from django.contrib import admin
from accounts.models import UserDetail
from django.contrib.sessions.models import Session

# registering models for admin
admin.site.register(UserDetail)

# # deleting undetected sessions
# Session.objects.all().delete()
