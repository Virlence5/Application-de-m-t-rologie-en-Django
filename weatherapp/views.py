from django.shortcuts import render

import datetime

def home(request) :

    if city in request.POST :
        city = request.POST['city']
    else :
        city = 'indore'

    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a5e3052e783e35b599ee1c5f6a31aa4"
    PARAMS = {'units', 'metric'}

    data = request.get(url, PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(request, "weatherapp/index.html", {
        'description' : description,
        'icon' : icon,
        'temp' : temp,
        'day' : day,
        'city' : city
    })