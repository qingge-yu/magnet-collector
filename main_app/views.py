from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Magnet

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def magnets_index(request):
    magnets = Magnet.objects.order_by('date')
    return render(request, 'magnets/index.html', {'magnets': magnets})


def magnets_detail(request, magnet_id):
    magnet = Magnet.objects.get(id=magnet_id)
    return render(request, 'magnets/detail.html', {'magnet': magnet})


class MagnetCreate(CreateView):
    model = Magnet
    fields = '__all__'
    success_url = '/magnets/'


class MagnetUpdate(UpdateView):
    model = Magnet
    fields = ['location', 'description', 'date']


class MagnetDelete(DeleteView):
    model = Magnet
    success_url = '/magnets/'
