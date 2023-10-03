from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bug
from .forms import BugForm

# Create your views here.

def index(request):
    bugs = Bug.objects.all()
    return render(request, 'index.html', {'bug_list': bugs})

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = BugForm()
    return render(request, 'bug_register.html', {'form': form})

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug_detail.html', {'bug': bug})
