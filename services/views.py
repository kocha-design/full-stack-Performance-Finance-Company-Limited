from django.shortcuts import render
from .models import Service

# def service_main(request):
#     return render(request, 'services/service.html')
 
# def services_home(request):
#     return render(request, 'services/services_home.html')

def biashara(request):
    bsn = Service.objects.filter(categories='biashara')
    return render(request, 'services/services/biashara.html', {'bsn': bsn})

def elimu(request):
    bsn = Service.objects.filter(categories='elimu')
    return render(request, 'services/services/elimu.html', {'bsn': bsn})

def kilimo(request):
    bsn = Service.objects.filter(categories='kilimo')
    return render(request, 'services/services/kilimo.html', {'bsn': bsn})

def nyumba(request):
    bsn = Service.objects.filter(categories='nyumba')
    return render(request, 'services/services/nyumba.html', {'bsn': bsn})

def vikundi(request):
    bsn = Service.objects.filter(categories='vikundi')
    return render(request, 'services/services/vikundi.html', {'bsn': bsn})

def waajiriwa(request):
    bsn = Service.objects.filter(categories='waajiriwa')
    return render(request, 'services/services/waajiriwa.html', {'bsn': bsn})
