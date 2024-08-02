from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('profile/<str:username>/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
]
