from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Magnet, Look
from .forms import ReviewForm

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
    id_list = magnet.looks.all().values_list('id')
    unused_looks = Look.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'magnets/detail.html', {
        'magnet': magnet,
        'review_form': review_form,
        'looks': unused_looks
    })


def add_review(request, magnet_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.magnet_id = magnet_id
        new_review.save()
    return redirect('detail', magnet_id=magnet_id)


def assoc_look(request, magnet_id, look_id):
    Magnet.objects.get(id=magnet_id).looks.add(look_id)
    return redirect('detail', magnet_id=magnet_id)


class MagnetCreate(CreateView):
    model = Magnet
    fields = ['name', 'location', 'description', 'date']
    success_url = '/magnets/'


class MagnetUpdate(UpdateView):
    model = Magnet
    fields = ['location', 'description', 'date']


class MagnetDelete(DeleteView):
    model = Magnet
    success_url = '/magnets/'


class LookList(ListView):
    model = Look


class LookDetail(DetailView):
    model = Look


class LookCreate(CreateView):
    model = Look
    fields = '__all__'


class LookUpdate(UpdateView):
    model = Look
    fields = '__all__'


class LookDelete(DeleteView):
    model = Look
    success_url = '/looks/'
