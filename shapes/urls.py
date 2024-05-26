# URL conf
from django.urls import path
from . import views


urlpatterns = [
    # ex: /shapes/
    path("", views.home, name = "home"),
    path("profile/", views.profile, name = "profile"),
    path("profile/USERNAME/post.id", views.shaooo, name = "detail"),
]


