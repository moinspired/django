from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
      if 'count' in session:
            print session['count']
            session['count'] += 1
      else:
            session['count'] = 1
      context = {
        "word": get_random_string(length=10)
        "count": request.session['count']
      }
      return render(request,'timedisplay/index.html', context)

def create(request):
    if request.method == "POST":
          return redirect("/")
    else:
          print "POST was not decected!!!!!!"