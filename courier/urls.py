from django.urls import path
from courier.views import CourierDayView, CourierDayCreateView, Home, UpdateCourierDay, DeleteCourierDay


urlpatterns = [
    path('courierday/', CourierDayView.as_view(), name='courier_day_view'),
    path('form/', CourierDayCreateView.as_view(), name='add_day_form'),
    path('', Home.as_view(), name='home'),
    path('courierday/update/<pk>', UpdateCourierDay.as_view(), name='update'),
    path('courierday/delete/<pk>', DeleteCourierDay.as_view(), name='delete'),
]