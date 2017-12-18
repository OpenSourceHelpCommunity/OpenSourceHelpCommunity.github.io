from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import chatSession, Contest, Journey
from .forms import ContestForm


def home(request):
    session_list = chatSession.objects.order_by('start_date')[:3]
    context_dict = {'chatSession': session_list}
    return render(request, 'index.html', context=context_dict)


def request_session(request):
    return render(request, 'session.html')


def contests(request):
    contest_list = Contest.objects.all()
    return render(request, 'contests.html',
                  context={'contest_list': contest_list})


def contest_new(request):
    form = ContestForm()
    return render(request, 'contest_edit.html', {'form': form})


def add_contest(request):
    if request.method == 'POST':
        form = ContestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/submit_contest/")
    else:
        form = ContestForm()
    return render(request, 'contest_edit.html', {'form': form})


def submit_contest(request):
    return render(request, 'contest_submission.html')


def journey(request):
    journey_list = Journey.objects.order_by('start_date')
    return render(request, 'journey.html',
                  context={'Journey': journey_list})
