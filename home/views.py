from django.shortcuts import render
import requests


# Create your views here.


def home(request):

    city=request.GET.get('city',"delhi")
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=056f75bb973d96794ac88af00ba0285f"
    data= requests.get(url).json()
    print(data)


    payload={
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':int(data['main']['temp']),
        'celcius_temperature':int(data['main']['temp'])-273,
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity']
        
        
    }

    context={'data':payload}
    print(context)

    
    
    
    
    return render(request,'home.html',context)