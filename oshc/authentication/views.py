from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse


def profile(request):
    return render(request, "profile.html")


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_present': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)