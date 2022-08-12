from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name ="homepage"),
    path("", include("podcasts.urls")),
    path("admin/", admin.site.urls),
]