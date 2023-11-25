from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, UserSerializer
from student.models import Student, User

# @api_view(["GET"])
# def LoggedInUserView(request):
#   user = User.objects.get(request.user)
#   user_ser = UserSerializer(User)
#   return Response(user_ser.data)

# Create your views here.
class LoggedInUserView(APIView):
  def get(self, request):
    serializer = UserSerializer(self.request.user)
    return Response(serializer.data)