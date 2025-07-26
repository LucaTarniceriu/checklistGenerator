from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import LoginForm
# Create your views here.
def authenticate(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("sent")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
