from django.contrib import admin

# Register your models here.
from app.models import Produit, Categorie, ProduitCategorie, Personne

admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(ProduitCategorie)
admin.site.register(Personne)