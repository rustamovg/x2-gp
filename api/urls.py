from django.urls import path
from .views import LoggedInUserView

app_name = 'api'

urlpatterns = [
  path('', LoggedInUserView.as_view(), name="user")
]