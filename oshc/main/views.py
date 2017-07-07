from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def request_session(request):
    return render(request, 'session.html')
