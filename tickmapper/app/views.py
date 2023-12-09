from django.shortcuts import render, HttpResponse
from django.db.models import Sum
from .models import route, tick
from .models import profile as profile_model
from .models import crag as crag_model
from django.contrib import messages
import requests
import os
from .ticks import crag_import

# Create your views here.
def home(request):
    return render(request, 'home.html')

def routes(request):
    if request.user.username:
        user = profile_model.objects.get(userName=request.user.username)
    else:
        user = '0'
    ticks = tick.objects.filter(user=user)
    total_len_ft = ticks.all().aggregate(Sum('height'))['height__sum']
    total_len_mi = total_len_ft / 5280.0
    return render(request, 'routes.html', {"ticks": ticks, 'total_len_ft': total_len_ft, 'total_len_mi': total_len_mi})

def map(request):
    crags = crag_model.objects.all()
    if request.user.username:
        user = profile_model.objects.get(userName=request.user.username)
    else:
        user = '0'

    ticks = tick.objects.filter(user=user)
    data = {}
    for crag in crags:
        data[crag.name] = {}
        data[crag.name]['lat'] = crag.lat
        data[crag.name]['lon'] = crag.lon
        data[crag.name]['ticks'] = list(tick.objects.filter(user=user).filter(crag=crag.id))
        #if len(data[crag.name]['ticks']) != 0:
            #print(crag.name, data[crag.name]['lat'],data[crag.name]['lon'], data[crag.name]['ticks'])
    return render(request, 'map.html', {'data' : data, 'crags': crags, 'ticks': ticks})


def handle_uploaded_file(file, username):
    path = './media/' + username + '.csv'
    #info = tick_import(username, path)
    with open(path, 'w') as f:
        try:
            f.write(file.read().decode('utf-8'))
        except:
            print('wrong file format: ' + file.name)
            os.remove(path)
            raise
    res = crag_import(username, path)
    return res


def import_ticks(request):
    if request.method == "POST":
            #add form validation
            res = {}
            if 'import' in request.FILES.keys():
                try:
                    res = handle_uploaded_file(request.FILES['import'], request.user.username)
                except:
                    messages.success(request,"file upload failed")
                    return render(request, 'import.html')
                messages.success(request, f'{res["ticks"]} ticks imported : {res["unique"]} unique crags : {res["new"]} new crags')
                return render(request,'import.html')
            else:
                messages.success(request,"no file selected")
                return render(request,'import.html')
    else:
        return render(request, 'import.html')

def profile(request):
    return render(request, 'profile.html')

