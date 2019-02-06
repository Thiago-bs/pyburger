from django.contrib import admin
from django.urls import path, include
from snackbar.api import *
from django.conf import settings
from tastypie.api import Api

api = Api(api_name=settings.REST_API_VERSION)

""" PYBURGER RESOURCES """
#api.register(snackbarResource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snackbar.urls')),
]
