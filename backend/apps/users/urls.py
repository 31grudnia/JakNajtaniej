from django.urls import path

from .views import CustomTokenObtaiPairView, CustomRefreshToken, UserLogoutAPI


urlpatterns = [    
    path('api/token/', CustomTokenObtaiPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', CustomRefreshToken.as_view(), name='token_refresh'), 
    path('api/logout', UserLogoutAPI.as_view(), name='user_logout'), 
]