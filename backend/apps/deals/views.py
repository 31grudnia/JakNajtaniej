from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..deals.models import Deal
from .serializer import DealSerializer


class DealsUserAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        deals = Deal.objects.filter(user=user)
        serializer = DealSerializer(deals, many=True)

        return Response(serializer.data)


