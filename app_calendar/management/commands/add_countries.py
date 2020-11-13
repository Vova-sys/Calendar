from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import requests
from tqdm import tqdm
from app_calendar.models import Country


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://www.officeholidays.com/countries"
        res = requests.get(url).text
        soup = BeautifulSoup(res)
        arr = [[j.text.strip() for j in i.find_all("a")] for i in soup.find_all("div", {"class": "four omega columns"})]
        all_arr = arr[0] + arr[1] + arr[2]

        for country in tqdm(all_arr):
            Country.objects.create(name=country)

