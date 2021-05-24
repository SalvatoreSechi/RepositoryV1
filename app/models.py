"""
Definition of models.
"""

from django.db import models

#Definisco la struttura

class Utente(models.Model):
    Nome = models.CharField(max_length=20)
    Cognome = models.CharField(max_length=20)
    Data_di_nascita = models.DateTimeField()
    Email = models.EmailField()
    Nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.Nickname

class Post(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    photo = models.ImageField()
    commenti = models.TextField()
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo