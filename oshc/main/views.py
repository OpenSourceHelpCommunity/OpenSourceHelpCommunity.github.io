from django.shortcuts import render
from django.http import HttpResponseRedirect

from main.models import chatSession, Contest

from datetime import datetime


def home(request):
    session_list = chatSession.objects.order_by('start_date')[:3]
    context_dict = {'chatSession': session_list}
    return render(request, 'index.html', context=context_dict)


def request_session(request):
    return render(request, 'session.html')


def contests(request):
    contest_list = Contest.objects.all()
    return render(request, 'contests.html', context={'contest_list':contest_list})


def contest_new(request):
    return render(request,'contest_edit.html')


def add_contest(request):

    contest = Contest()
    contest.name = request.POST.get("name", "null")
    contest.link = request.POST.get("link", "null")
    start_date = request.POST.get("start_date","null")
    end_date = request.POST.get("end_date", "null")
    contest.description = request.POST.get("desc", "null")

    contest.end_date=datetime.strptime(end_date,'%Y-%m-%d').date()
    contest.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()

    contest.save()

    return HttpResponseRedirect("/contests/")