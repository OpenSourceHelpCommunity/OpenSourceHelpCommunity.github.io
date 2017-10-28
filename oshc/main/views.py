from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import chatSession, Contest
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
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


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler403(request):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response
