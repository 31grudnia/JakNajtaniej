from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

from .views import CustomTokenObtaiPairView


urlpatterns = [    
    path('api/token/', CustomTokenObtaiPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]