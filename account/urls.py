from django.urls import path
from .views import *
from .views import EmailCheckView, UserProfileViewSet

user_profile_update = UserProfileViewSet.as_view({
    'put': 'update',
})

urlpatterns = [
    path("check-email/", EmailCheckView.as_view(), name="check-email"),
    path('users/<int:pk>/profile/', user_profile_update, name='user-profile-update'),
    ]