from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class SomeProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return JsonResponse({'message': 'This is a protected view'})
def index(request):
    return HttpResponse("Hello, welcome to the index page!")

class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = {
            'id': user.id,
            'username': user.username,
            # other user fields
        }
        return JsonResponse(data)

