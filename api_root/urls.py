from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include("gossip_api.urls"), name= "gossip_api"),
]
