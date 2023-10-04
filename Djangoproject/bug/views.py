from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bug
from .forms import BugForm

# Create your views here.

def index(request):
    """
    Render the index page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the rendered index page.
    """
    bugs = Bug.objects.all()
    return render(request, 'index.html', {'bug_list': bugs})

def register_bug(request):
    """
    Register a bug.

    Parameters:
    - `request` (HttpRequest): The HTTP request object.

    Returns:
    - `HttpResponse`: The HTTP response object.

    Description:
    This function is used to register a bug. If the request method is 'POST',
    it validates the bug form and saves it. If the form is valid, it redirects
    to the index page. If the request method is not 'POST', it creates a new
    bug form and renders the 'bug_register.html' template with the form.

    Example usage:
    register_bug(request)
    """
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = BugForm()
    return render(request, 'bug_register.html', {'form': form})

def view_bug(request, bug_id):
    """
    Renders the bug detail page.

    Args:
        request (HttpRequest): The HTTP request object.
        bug_id (int): The ID of the bug to view.

    Returns:
        HttpResponse: The HTTP response object containing the rendered bug detail page.
    """
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug_detail.html', {'bug': bug})
