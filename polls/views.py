from django.shortcuts import render, HttpResponse
from django.views import View
from datetime import datetime
from .models import temp_read, water_level, soil_moisture
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getdata(request):
    temp = request.GET['t']
    level = request.GET['cm']
    moisture = request.GET['m']
    obj = temp_read()
    obj.temp = temp
    obj.dt = datetime.now()
    obj.save()        
    obj = water_level()
    obj.level = level
    obj.save()        
    obj = soil_moisture()
    obj.m_level = moisture
    obj.dt = datetime.now()
    obj.save()
    return HttpResponse('this is a get request')


'''class temp_sense(View):

    @csrf_exempt
    def getdata(request):
        temp = request.GET['t']
        obj = temp_read()
        obj.temp = temp
        obj.dt = datetime.now()
        obj.save()
        return HttpResponse('this is a get request')
        
        
    def post(self, request, *args, **kwargs):
        
        temp = request.POST.get("temperature", "")
        obj = temp_read()
        obj.temp = temp
        obj.save()
        print('Data was sent successfully')
        return HttpResponse('DONE')


class water_sense(View):
    def getdata(request):
        level = request.GET['cm']
        obj = water_level()
        obj.level = level
        obj.save()
        return HttpResponse('this is a get request')

    def post(self, request, *args, **kwargs):
        temp = request.POST.get("water", "")
        obj = water_level()
        obj.level = temp
        obj.save()
        print('Data was sent successfully')
        return HttpResponse('DONE')


class soil_sense(View):
    def getdata(request):
        moisture = request.GET['m']
        moisture = soil_moisture()
        obj.m_level = moisture
        obj.dt = datetime.now()
        obj.save()
        return HttpResponse('this is a get request')

    def post(self, request, *args, **kwargs):
        temp = request.POST.get("soil_moisture", "")
        obj = soil_moisture()
        obj.m_level = temp
        obj.save()
        print('Data was sent successfully')
        return HttpResponse('DONE')
'''

def index(request):
    latest_temp_list = temp_read.objects.all()
    water_l = water_level.objects.all()
    soil_m_l = soil_moisture.objects.all()
    context = {'latest_temp_list': latest_temp_list, 'water_l': water_l, 'soil_m_l': soil_m_l}
    return render(request, 'polls/index.html', context)


