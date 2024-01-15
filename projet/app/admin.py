from django.contrib import admin

# Register your models here.
from .models import produit,client,fournisseur,centre,employe,absence,avanceSalaire,venteProduit,paiementCredit

admin.site.register(client)
admin.site.register(fournisseur)
admin.site.register(centre)
admin.site.register(employe)
admin.site.register(absence)
admin.site.register(avanceSalaire)
admin.site.register(produit)
admin.site.register(venteProduit)
admin.site.register(paiementCredit)