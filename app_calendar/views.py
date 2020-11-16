from calendar import Calendar

from django.http import request
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView

from app_calendar.models import Country, Holiday
from app_calendar.serialize import CountrySerializer, HolidaySerializerRead, HolidaySerializerWrite


class ListCountries(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_fields = ['name']

    # def get_queryset(self):
    #     if self.kwargs.get('name'):
    #         return Country.objects.filter(id=self.kwargs.get('name'))
    #     return Country.objects.all()


class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializerRead
    queryset = Holiday.objects.all()
    filter_fields = ['country']

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Holiday.objects.filter(country=self.kwargs.get('id'))
        return Holiday.objects.all()


class CreateHolidays(CreateAPIView):
    serializer_class = HolidaySerializerWrite
