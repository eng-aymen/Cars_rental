from django.shortcuts import render
from Cars.models import Car,CarType

# Create your views here.
def index(request):

    context ={
        'car':Car.objects.all(),
        'car_type':CarType.objects.all(),
    }
    
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')