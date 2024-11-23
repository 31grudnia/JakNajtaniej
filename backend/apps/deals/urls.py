from django.urls import path

from .views import DealsUserAPI

urlpatterns = [
    path('your-deals/', DealsUserAPI.as_view(), name="authenticated-user-deals")
]