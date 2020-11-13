from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from app_calendar.models import Holiday, Country, Event, User

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class HolidaySerializerRead(ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = Holiday
        fields = '__all__'

class HolidaySerializerWrite(ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

