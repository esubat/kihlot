from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView,UserProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<str:username>/', UserDetailView.as_view(), name='user_detail'),
    path('update/',UserProfileUpdateView.as_view() , name ='profile_update'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
]
