"""
Definition of urls for Django_Prova.
"""
from django.conf.urls.static import static
from django.conf import settings
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.Home, name='home'), #importo la views e gli passo il parametro nome che è uguale a home
    path('creazione_post', views.creazione_post, name='crea_post'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('visualizza_post/', views.visualizza_post ,name = 'VisualizzaPost'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)