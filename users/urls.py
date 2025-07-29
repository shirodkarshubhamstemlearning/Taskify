# from django.urls import path
# from .views import RegisterView, LoginView, LogoutView, CustomPasswordResetView
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]


from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, ProfileAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]

