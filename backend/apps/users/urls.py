from django.urls import path

from .views import CustomTokenObtaiPairView, CustomRefreshToken, UserLogoutAPI, UserRegisterAPI


urlpatterns = [    
    path('api/token/', CustomTokenObtaiPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', CustomRefreshToken.as_view(), name='token_refresh'), 
    path('api/logout', UserLogoutAPI.as_view(), name='user_logout'), 
    path('api/register', UserRegisterAPI.as_view(), name='user_register'), 
]