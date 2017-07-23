from django.shortcuts import render

from main.models import chatSession


def home(request):
    session_list = chatSession.objects.order_by('start_date')[:3]
    context_dict = {'chatSession': session_list}
    return render(request, 'index.html', context=context_dict)


def request_session(request):
    return render(request, 'session.html')
