from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Car,Booking,CarType
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import EmailCarForm
from django.core.mail import send_mail
from django.contrib import messages
from taggit.models import Tag
from datetime import date

# Create your views here.


def car_share(request, car_id):
    try:
        # Retrieve car by id
        car = get_object_or_404(Car, id=car_id)
        sent = False
        if request.method == 'POST':
        # Form was submitted
            form = EmailCarForm(request.POST)
            if form.is_valid():
        # Form fields passed validation
                cd = form.cleaned_data
                car_url = request.build_absolute_uri(car.get_url())
                subject = f"{cd['name']} recommends you read " \
                f"{car.c_name}"
                message = f"Read {car.c_name} at {car_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, 'crental583@gmail.com',
                [cd['to']])
                sent = True
        # ... send email
        else:
            form = EmailCarForm()
    except:
        messages.error(request,'Check your internet connection then try again')
        return render(request, 'cars/share.html')

    return render(request, 'cars/share.html', {'car': car,
                'form': form,
                'sent': sent})

# class CarListView(ListView):
#     """
#     Alternative post list view
#     """
#     queryset = Car.objects.all().filter(c_status = True)
#     context_object_name = 'car'
#     paginate_by = 3
#     template_name = 'cars/cars.html'


def cars(request,tag_slug=None):
    car_list = Car.objects.all().filter(c_status = True)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        car_list = car_list.filter(tags__in=[tag])

    if 'select' in request.GET:
        select = request.GET['select']
        if select:
            ct = CarType.objects.get(ct=select)
            car_list = car_list.filter(c_type = ct)
    
    if 'name' in request.GET:
        name=request.GET['name']
        if name:
            car_list=car_list.filter(c_name__icontains=name)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            car_list = car_list.filter(c_model = model)

    #paginator
    paginator = Paginator(car_list,3)
    page_number = request.GET.get('page',1)
    car = paginator.page(page_number)
    return render(request,'cars/cars.html',{'car':car,'tag': tag})

def details(request,year,month,day,car):
    context = {
        'c':get_object_or_404(Car, c_slug=car,
                              c_publish__year=year,
                              c_publish__month=month,
                              c_publish__day=day)
    }
    return render(request,'cars/details.html',context)

def rentcar(request):
    if  'phone' in request.GET and 'exdate' in request.GET and 'c_id' in request.GET and 'price' in request.GET:
        if Car.objects.all().filter(id=request.GET['c_id'],c_status=True).exists():
            name = request.user.first_name +' '+ request.user.last_name
            phone = request.GET['phone']
            exdate = request.GET['exdate']
            c_id = request.GET['c_id']
            car = Car.objects.get(id=request.GET['c_id'])
            price = car.c_price
            if car:
                booking = Booking.objects.create(b_car=car,b_name=name,b_phone=phone,b_exdate=exdate)
                car.c_status = False
                car.save()
                messages.success(request,car.c_name + '  was rented for '+ name)
        else:
            messages.error(request,"You can't rent this car ,because it is rented before")
    else:
        messages.error(request,"There is something wrong")

    return redirect('cars')

def bookings(request):
    if request.user.is_authenticated and request.user.is_staff:
        bookings = Booking.objects.all().filter(b_status=True)
        context = {
                    'bookings': bookings,
                    'd':date.today(),
                   }
        return render(request,'admin/bookings.html',context)
    return redirect('/admin/')

def expire(request):
    bookings = Booking.objects.get(id=request.GET['b_id'],b_status=True)
    bookings.b_status = False
    bookings.b_car.c_status = True
    bookings.b_car.save()
    bookings.save()

    messages.success(request,"Expiring reserce is done")
    return redirect('bookings')