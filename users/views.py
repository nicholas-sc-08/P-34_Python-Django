from django.shortcuts import render
from django.http import JsonResponse
from users.models import User

# Create your views here.

def userList(request):
    users = User.objects.all()
    userData = [{"name": user.name, "email": user.email, "passowrd": user.password} for user in users]
    return JsonResponse(userData, safe=False)