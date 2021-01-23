from django.urls import path
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", views.index, name="index"),
    path("about/", views.intro, name="about"),
    path("faq/", views.faqq, name="faq"),
    path("gallery/", views.galleryphotos, name="gallery"),
    path("staff/", views.members, name="staff"),
    path("certificates/", views.cert, name="certificate"),
    path("sops/", views.sops, name="sops"),
    path("pastevents/", views.pastevents, name="pastevents"),
    path("upcomingevents/", views.upevents, name="upcomingevents"),
    path("guidelines/", views.guidelines, name="guidelines"),
    path("announcements/", views.announcements, name="announcements"),
    path("synopsis/", views.projectsynopsis, name="synopsis"),
    path("non-synopsis/", views.projectnonsynopsis, name="non-synopsis"),
    path("projectpost/<int:id>", views.projectpost, name="projectposts"),
    path("contact/", views.contacts, name="Contact"),
    path('',RedirectView.as_view(url="index/")),
]
