from django.urls import path
from .views import dashboard, register, student_login, student_logout

app_name = 'student'

urlpatterns = [
  path('register/', register, name='register'),
  path('login/', student_login, name='login'),
  path('logout/', student_logout, name='logout'),
  path('', dashboard, name='home'),
]