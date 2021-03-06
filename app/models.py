from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=200,
                           default=None,
                           blank=True,
                           help_text='La catégorie')

class Produit(models.Model):
    nom = models.CharField(max_length=200,
                           default=None,
                           blank=True,
                           help_text='Le cadeau')
    detail = models.TextField(default=None,
                              blank=True,
                              null=True)
    prix = models.FloatField(default=0.0, blank=True)
    votes = models.ManyToManyField('Personne',
                                   default=None,
                                   blank=True)
    categories = models.ManyToManyField(
        Categorie, blank=True, default=None,
        through='ProduitCategorie')

    def __str__(self):
        return '{} ({})'.format(self.nom, self.prix)

class ProduitCategorie(models.Model):
    categorie = models.ForeignKey(Categorie,
                                  on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit,
                                on_delete=models.CASCADE)


class Personne(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cadeaux = models.ManyToManyField(Produit,
                                     blank=True,
                                     default=None)
    contributions = models.ManyToManyField(Produit,
                                           related_name='contributions',
                                           default=None,
                                           blank=True)

