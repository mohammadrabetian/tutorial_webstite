from django.shortcuts import render
from main.models import Tutorial


def homepage(request):
    return render(request, 'main/home.html', {'tutorials': Tutorial.objects.all()})
