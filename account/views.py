from utils.validation_utils import is_valid_email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserUpdateSerializer

class EmailCheckView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if noy is_valid_email(email):
            return Response({"error": "Ivalid email address"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Valid email!"}, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self, request, pk=None):
        # Ensure user can update only their own profile
        if str(request.user.pk) != pk:
            return Response({"error": "You can only update your own profile."}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserUpdateSerializer(user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)