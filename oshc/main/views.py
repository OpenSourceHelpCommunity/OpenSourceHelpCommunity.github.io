from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import chatSession, Contest, Journey
from .forms import ContestForm


def home(request):
    # chat_session_list = chatSessions.objects.order_by('start_date')[:3]
    # context_dict = {'chatSessions': chat_session_list}
    return render(request, 'index.html')


def request_session(request):
    return render(request, 'session.html')


def contests(request):
    contest_list = Contest.objects.all()
    return render(
        request, 'contests.html', context={
            'contest_list': contest_list
        })


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

def chat_sessions(request):
    chat_session_list = chatSession.objects.all()
    return render(request, 'chatsessions.html',
                  context={'chat_session_list': chat_session_list})


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def journey(request):
    journey_list = Journey.objects.order_by('start_date')
    return render(request, 'journey.html', context={'Journey': journey_list})
  
def jobs(request):
    return render(request, 'jobs.html')
