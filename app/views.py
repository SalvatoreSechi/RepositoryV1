"""
Definition of views. 
"""
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PostForm
from django.http import HttpResponse
from .models import Post 
from django.contrib.auth.decorators import login_required

#Definisco la logica

def Home(request):  #definisco una home
    return render(request, "app/Home.html") #associo la pagina home.html all'app
        

@login_required(login_url='login')
def creazione_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            nuovo_post = form.save()
            return redirect('VisualizzaPost')
    else:
        form = PostForm()

    context = {"form": form}
    return render (request, "app/creazione_post.html", context)

@login_required(login_url='login')
def visualizza_post(request):
    posts = Post.objects.order_by('-pk')
    context = { "posts" : posts }

    return render (request, "app/visualizza_post.html", context)

#def login(request):
    #return render(request, "app/login.html") 

#def Register(request):
    #return render(request, "app/Register.html")

#def home(request):
#   return render(request, "app/home.html")
#   """Renders the home page."""
#   assert isinstance(request, HttpRequest)
#   return render(
#       request,
#       'app/index.html',
#       {
#           'title':'Home Page',
#           'year':datetime.now().year,
#       }

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
