from student.models import User, Student

def get_user(request):
  if request.user.is_authenticated:
    return {
      'user': request.user
    }
  else:
    return {
      'user': None
    }