from django.shortcuts import HttpResponse
from django.shortcuts import render



def home(request):

    return render(request, "polls/landing.html", {})

