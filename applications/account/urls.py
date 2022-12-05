from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from applications.account.views import RegisterAPIView, ChengePasswordApiView, send_hello_api_view, ActivationApiViewA, \
    ForgotPasswordAPIView, ForgotPasswordCompleteAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    # path('login/', LoginApiView.as_view()),
    # path('logout/', LogoutApiView.as_view()),

    path('change_password/', ChengePasswordApiView.as_view()),
    path('send_mail/', send_hello_api_view),
    path('activate/<uuid:activation_code>/', ActivationApiViewA.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteAPIView.as_view())
]