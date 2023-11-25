from django import forms
from .models import User, Student
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password']

class ExtendedUserCreationForm(UserCreationForm):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
      user = super().save(commit=False)

      user.first_name = self.cleaned_data['first_name']
      user.last_name = self.cleaned_data['last_name']

      if commit:
        user.save()
      return user
    
class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('fathers_name','faculty','field_of_education','group','education_stage')