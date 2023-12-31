from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="Home"),
    path("about/",views.about, name="AboutUs"),
    path("contact/",views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name="TrackingStatus"),
    path("search/",views.search, name="Search"),
    path("productview/",views.productview, name="ProductView"),
    path("cheakout/",views.cheakout, name="CheakOut")
]