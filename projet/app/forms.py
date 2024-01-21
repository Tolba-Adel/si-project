from django.db.models import fields
from django import forms
from .models import client,fournisseur,centre,employe,produit,venteProduit,paiementCredit

class clientForm(forms.ModelForm):
    class Meta:
        model = client
        fields="__all__"
        labels = {
            'nomCl': 'Nom',
            'prenomCl': 'Prénom',
            'adresseCl': 'Adresse',
            'telephoneCl': 'Telephone'
        }

class fournisseurForm(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields="__all__"
        labels = {
            'nomF': 'Nom',
            'prenomF': 'Prénom',
            'adresseF': 'Adresse',
            'telephoneF': 'Telephone'
        }

class employeForm(forms.ModelForm):
    class Meta:
        model = employe
        exclude=['points']
        labels = {
            'nomE': 'Nom',
            'prenomE': 'Prénom',
            'adresseE': 'Adresse',
            'telephoneE': 'Telephone',
            'salaire_jour': 'Salaire journalier',
            'centre': 'Centre'
        }

class produitForm(forms.ModelForm):
    class Meta:
        model=produit
        fields="__all__"
        lables={
            'nomP':'Nom produit',
            'qte':'Quantité',
        }

class venteProduitForm(forms.ModelForm):
    class Meta:
        model=venteProduit
        exclude=['centre']
        labels={
            'dateVente':'Date',
            'produitVendu':'Produit',
            'qteVendu':'Quantité',
            'prixVente':'Prix Unitaire',
            'montantVerse':'Montant Versé'
        }

class paiementCreditForm(forms.ModelForm):
    class Meta:
        model=paiementCredit
        exclude=['client']
        labels={
            'datePaiement':'Date',
            'montantPaiement':'Montant du Paiement'
        }