from django.urls import path

from .views import CustomTokenObtaiPairView, CustomRefreshToken


urlpatterns = [    
    path('api/token/', CustomTokenObtaiPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', CustomRefreshToken.as_view(), name='token_refresh'), 
]