from utils.validation_utils import is_valid_email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class EmailCheckView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if noy is_valid_email(email):
            return Response({"error": "Ivalid email address"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Valid email!"}, status=status.HTTP_200_OK)