from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display = ('field_of_education', 'group', 'education_stage', 'faculty')
    list_filter = ('field_of_education', 'group', 'education_stage', 'faculty')