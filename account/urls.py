from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from account.views import RegistrationView, ActivationView, LogoutView, ForgotPasswordView, CompleteRestPasswordView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:email>/<str:code>', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout_token/', LogoutView.as_view(), name='logout_token'),
    path('forgot_password/<str:email>/', ForgotPasswordView().as_view()),
    path('complete_recovery/', CompleteRestPasswordView().as_view())
]
