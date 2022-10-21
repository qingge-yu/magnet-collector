from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


class Magnet:
    def __init__(self, name, location, description, date):
        self.name = name
        self.location = location
        self.description = description
        self.date = date


magnets = [
    Magnet('Salzburg', 'Germany', 'Shaped like a beer mug', 2015),
    Magnet('Yosemite National Park', 'California',
           'A picture of Half Dome', 2018),
    Magnet('Honolulu', 'Hawaii', 'Aloha gesture with spring so it moves', 2021)
]


def home(request):
    return HttpResponse("<h1>Let's collect some magnets!</h1>")


def about(request):
    return render(request, 'about.html')


def magnets_index(request):
    return render(request, 'magnets/index.html', {'magnets': magnets})
