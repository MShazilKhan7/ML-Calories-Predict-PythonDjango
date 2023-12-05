from django.shortcuts import render, HttpResponse
from calories.models import CaloriesData



def predict_calories(request):
    context = {}
    if request.method == 'POST':
        gender    = request.POST.get('gender')
        age       = request.POST.get('age')
        height    = request.POST.get('height')
        weight    = request.POST.get('weight')
        duration  = request.POST.get('duration')
        heartrate = request.POST.get('heartrate')
        bodytemp  = request.POST.get('bodytemp')

        print(gender,age,height,weight,duration,heartrate,bodytemp)
        data = CaloriesData(gender=gender,age=age, height=height, weight=weight, duration=duration, heartRate=heartrate, bodyTemp=bodytemp)
        data.save()
        context['prediction']=data.calories
        print(data.gender)
        return render(request, 'success.html', context)
    return render(request, 'calories.html')


def home(request):
    return render(request, 'home.html')