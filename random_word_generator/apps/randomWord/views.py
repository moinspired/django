from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
      if 'count' in  request.session:
            request.session['count'] += 1
      else:
             request.session['count'] = 1
      context = {
        "word": get_random_string(length=10),
        "num": request.session['count']
      }
      print 
      return render(request,'randomWord/index.html', context )

def generate(request):
    request.session['tries'] += 1  
    return redirect('/')