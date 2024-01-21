from django.contrib import admin

# Register your models here.
from .models import produit,client,fournisseur,centre,employe,matierePremiere,achat, TransfertMatierePremiere,ReglementFournisseur,VenteMatierePremiere,PaiementCredit,Stock
admin.site.register(client)
admin.site.register(fournisseur)
admin.site.register(employe)
admin.site.register(centre)
admin.site.register(produit)
admin.site.register(matierePremiere)
admin.site.register(achat)
admin.site.register(TransfertMatierePremiere)
admin.site.register(ReglementFournisseur)
admin.site.register(VenteMatierePremiere)
admin.site.register(PaiementCredit)
admin.site.register(Stock)