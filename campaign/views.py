from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
     
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, you are fully authenticated, eveyrthing works fine!'}

        return Response(content)