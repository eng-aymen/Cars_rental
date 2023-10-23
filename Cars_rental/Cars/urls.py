from django.urls import path
from . import views

urlpatterns = [
    path('',views.cars,name='cars'),
    path('tag/<slug:tag_slug>/',views.cars, name='car_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:car>',views.details,name='details'),
    path('<int:car_id>/share/',views.car_share, name='car_share'),
    path('rentcar/',views.rentcar,name='rentcar'),
    path('bookings/',views.bookings,name='bookings'),
    path('expire',views.expire,name='expire'),
]