from rest_framework import serializers
from student.models import User, Student

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('first_name', 'last_name')

class StudentSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Student
    fields = ["user","fathers_name", "faculty", "field_of_education", "group", "education_stage"]
    depth = 1