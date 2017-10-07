from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import UsersData
from polls.models import temp_read, soil_moisture, water_level


def tutorial(request):
    return render(request, 'users/tutorial.html', {})


def signup(request):
    return render(request, 'users/signup-page.html', {})


def profile(request):
    return render(request, 'users/profile-page.html', {})


def makeUser(request):
    allUser = UsersData.objects.all()
    uobj = UsersData()
    uobj.name = request.POST['name']
    uobj.email = request.POST['email']
    for user in allUser:
        if user.email == uobj.email:
            return render(request, 'users/signup-page.html', {'error': 'error', })
    uobj.password = request.POST['password']
    uobj.save()
    return HttpResponseRedirect(reverse('users:login'))


def login(request):
    return render(request, 'users/login-page.html', {})

def graph(request):
    temp_list = temp_read.objects.all()
    soil_list = soil_moisture.objects.all()
    water_list = water_level.objects.all()
    return render(request, 'users/graph.html', {'temp_list': temp_list, 'soil_list': soil_list, 'water_list': water_list, })


def sensors(request):
    temp_list = temp_read.objects.all()
    soil_list = soil_moisture.objects.all()
    water_list = water_level.objects.all()
    return render(request, 'users/sensors.html',
            {'temp_list': temp_list, 'soil_list': soil_list, 'water_list': water_list, })


def weather(request):
    return render(request, 'users/weather/index.html', {})


def contact(request):
    return render(request, 'users/weather/contact.html', {})

def water(request):
    return render(request, 'users/water.html', {'water_list':water_level.objects.all()})

def logout(request):
    return HttpResponseRedirect(reverse('users:login'))


def UserProfile(request):
    st = request.POST['email']
    pt = request.POST['password']
    allusers = UsersData.objects.all()
    for users in allusers:
        if users.email == st:
            return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'users/login-page.html', {'error': 'error', })


