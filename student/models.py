from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  fathers_name = models.CharField(max_length=100, verbose_name='Otasini ismi')
  faculty = models.CharField(max_length=500, verbose_name="Fakultet")
  field_of_education = models.CharField(max_length=500, verbose_name="Ta'lim yo'nalishi")
  group = models.CharField(max_length=500, verbose_name="Guruhi")
  education_stage = models.IntegerField(verbose_name="Ta'lim bosqichi")

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name} {self.fathers_name} o'g'li"

  