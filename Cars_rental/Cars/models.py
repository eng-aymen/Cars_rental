from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class CarType(models.Model):
    ct = models.CharField(max_length=30)

    def __str__(self):
        return self.ct

class Car(models.Model):
    c_name = models.CharField(max_length=30)
    c_price = models.IntegerField()
    c_slug = models.SlugField(blank=True,null=True,unique_for_date='c_publish')
    c_model = models.IntegerField()
    c_status = models.BooleanField(default=True)
    c_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    c_details = models.TextField(null=True)
    c_publish = models.DateTimeField(null=True,default=timezone.now)
    c_type = models.ForeignKey(CarType,on_delete=models.CASCADE)
    tags = TaggableManager()
    def get_url(self):
        return reverse('details',args=[self.c_publish.year,
                                       self.c_publish.month,
                                       self.c_publish.day,
                                       self.c_slug])

    def __str__(self):
        return self.c_name
    
class Booking(models.Model):
    b_name = models.CharField(max_length=30)
    b_phone = models.BigIntegerField()
    b_date = models.DateTimeField(default=timezone.now)
    b_exdate = models.DateField()
    b_status = models.BooleanField(default=True)
    b_car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='cars_bookings')

    def __str__(self):
        return self.b_name

