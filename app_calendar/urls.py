from django.urls import path

from app_calendar import views

urlpatterns = [
    path('countries/', views.ListCountries.as_view(), name='countrieslist'),
    path('holidays/', views.ListHolidays.as_view(), name='ListHolidays'),
    path('holidayslist/<int:country>/', views.ListHolidays.as_view(), name='holidays_country_list'),

]

