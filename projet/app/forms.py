from django.db.models import fields
from django import forms
from .models import client,fournisseur,centre,employe,matierePremiere

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

class centreForm(forms.ModelForm):
    class Meta:
        model = centre
        fields="__all__"
        labels = {
            'nomC': 'Nom',
            'numeroC':'Numéro'
        }

class employeForm(forms.ModelForm):
    class Meta:
        model = employe
        # fields="__all__"
        exclude=['points']
        labels = {
            'nomE': 'Nom',
            'prenomE': 'Prénom',
            'adresseE': 'Adresse',
            'telephoneE': 'Telephone',
            'salaire_jour': 'Salaire journalier',
            'centre': 'Centre'
        }

class matierePremiereForm(forms.ModelForm):
    class Meta:
        model = matierePremiere
        fields="__all__"
        labels = {
            'nomMP': 'Nom',
            'prix_achatMP': "Prix d'achat",
            'prix_venteMP': "Prix de vente"
        }

