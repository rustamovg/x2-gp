from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ExtendedUserCreationForm, StudentForm, LoginForm
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = ExtendedUserCreationForm(request.POST)
    student_form = StudentForm(request.POST)
    if form.is_valid():
      user = form.save()
      student = student_form.save(commit=False)
      student.user = user
      student.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username = username, password = password)
      login(request, user)
      return redirect('student:home')
  else:
    form = ExtendedUserCreationForm()
    student_form = StudentForm()
  context={'form':form, 'student_form':student_form}
  return render(request, 'student/register.html', context)

def student_login(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    user = authenticate( username=form.data['username'], password=form.data['password'])
    if user is not None:
      login(request, user)
      return redirect("student:home")
    else:
      return render(request, 'student/login.html', {'form':form})
  return render(request, 'student/login.html', {'form':form})

def student_logout(request):
  logout(request)
  return redirect('student:login')

@login_required(login_url='student:login')
def dashboard(request):
  context = {}
  return render(request, 'student/dashboard.html', context)