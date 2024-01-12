from django.contrib import admin

# Register your models here.
from .models import produit,client,fournisseur,centre,employe

admin.site.register(client)
admin.site.register(fournisseur)
admin.site.register(employe)
admin.site.register(centre)
admin.site.register(produit)