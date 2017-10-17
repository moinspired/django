from django.shortcuts import render, HttpResponse,redirect


def index(request):
    return render(request,'form/index.html')

def create(request):
    if request.method == "POST":
     context = {
        'first' : request.POST['firstname'],
        'last' : request.POST['lastname'],
        'desc' : request.POST['desc'],
     }
    return render(request,'form/info.html', context)

def summary(request):
    return redirect('/')