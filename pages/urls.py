from django.urls import path
from .views import (
    home,vision,about,contact,page_view
)
urlpatterns=[
path("",home, name="home"),
path("vision/",vision, name="vision"),
# path("contact/",contact,name="contact"),
# path("about/",about, name="about"),
path("<slug:slug>/",page_view),
]