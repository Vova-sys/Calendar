from calendar import Calendar

from django.http import request
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from app_calendar.models import Country, Holiday
from app_calendar.serialize import CountrySerializer, HolidaySerializerRead


class ListCountries(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        if self.kwargs.get('name'):
            return Country.objects.filter(id=self.kwargs.get('name'))
        return Country.objects.all()


class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializerRead

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Holiday.objects.filter(country=self.kwargs.get('id'))
        return Holiday.objects.all()


class CountriesFilter(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']

