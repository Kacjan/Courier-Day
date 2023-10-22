from django.urls import path
from courier.views import CourierDayListView, CourierDayCreateView, Home, UpdateCourierDay, DeleteCourierDay

urlpatterns = [
    path('courierday/', CourierDayListView.as_view(), name='courier_day_list_view'),
    path('form/', CourierDayCreateView.as_view(), name='add_day_form'),
    path('', Home.as_view(), name='home'),
    path('courierday/update/<pk>', UpdateCourierDay.as_view(), name='update'),
    path('courierday/delete/<pk>', DeleteCourierDay.as_view(), name='delete'),
]