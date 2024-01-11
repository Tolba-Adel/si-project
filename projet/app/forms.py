from django.db.models import fields
from django import forms
from .models import client,fournisseur,centre,employe,matierePremiere,achat,TransfertMatierePremiere,ReglementFournisseur,VenteMatierePremiere
import calculation
from django_select2 import forms as s2forms


centre_possibles=[
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]

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

class fournisseurWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomF__icontains",
    ]

class matieresAchetesWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomMP__icontains",
    ]

class AchatmatierePremiereForm(forms.ModelForm):
   
    montantTotal=forms.IntegerField(widget=calculation.FormulaInput('QteAchat*prixAchat', attrs={'readonly': 'readonly'}),label='Montant Total',disabled=False, required=False  )
    montantRestant=forms.IntegerField(widget=calculation.FormulaInput('montantTotal - montantverse', attrs={'readonly': 'readonly'}),label='Montant Restant',disabled=False, required=False  )

    class Meta:
        model = achat
        fields="__all__"
        labels = {
            'dateAchat': 'Date Achat',
            'fournisseur': "Fournisseur",
            'matieresAchetes.nomMP': "Matiere Premiere",
            'QteAchat':'Quantite achetée',
            'prixAchat':'prix Achat',
            'montantTotal': 'Montant Total',
            'montantverse':'Montant versé',
            'montantRestant':'Montant Restant'
        }


        widgets = {
            "fournisseur": fournisseurWidget,
            "matieresAchetes": matieresAchetesWidget,
        }

class TransfertmatierePremiereForm(forms.ModelForm):
    centre=centre.numeroC
    MatieresTransferes = forms.ModelChoiceField(
         queryset=achat.objects.prefetch_related('matieresAchetes'),
    )
    PrixUTA = forms.IntegerField(widget=forms.HiddenInput(),label='Cout de Transfert',disabled=False, required=False  )
    CoutTrf=forms.IntegerField(widget=forms.HiddenInput(),label='Cout de Transfert',disabled=False, required=False)
    
    
    
    class Meta:
        model = TransfertMatierePremiere
        fields="__all__"
        labels = {
            'dateTransfert': 'Date Transfert',
            'centre': 'Numero centre',
            'MatieresTransferes': 'Matieres Transferes',
            'QteTrf':'Quantité',
            'PrixUTA':'Prix Unitaire',
            'CoutTrf':'Cout de Transfert'
        }
    

class ReglementMPForm(forms.ModelForm):
    solde=forms.FloatField(widget=calculation.FormulaInput('montantRestant*1', attrs={'readonly': 'readonly'}),label='solde',required=False)
   
    class Meta:
        model = ReglementFournisseur
        fields="__all__"
        labels = {
            'dateReg': 'Date Reglement',
            'Fournisseur': "Nom Fournisseur",
            'solde' : 'solde fournisseur',
            'montantReg': "Montant Reglement",
  
        }

class matieresVendueWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomMP__icontains",
    ]
class VentematierePremiereForm(forms.ModelForm):
    montantVente=forms.FloatField(widget=calculation.FormulaInput('QteVds*prixUT', attrs={'readonly': 'readonly'}),label='Montant Total',disabled=False, required=False  )
    ResteAPayer=forms.FloatField(widget=calculation.FormulaInput('montantVente - montantEncaisse', attrs={'readonly': 'readonly'}),label='Montant Restant',disabled=False, required=False  )

    
    class Meta:
        model = VenteMatierePremiere
        fields="__all__"
        labels = {
            'dateVente': 'Date de Vente',
            'client': 'Nom Client',
            'MPVendus': 'Matiere Premiere',
            'QteVds': 'Quantite vendue',
            'prixUT': 'Prix de Vente',
            'montantVente': 'Montant de Vente',
            'montantEncaisse':'Montant Encaissé',
            'ResteAPayer': 'Reste à payer',
        }

        widgets = {
            "MPVendus": matieresVendueWidget,
        }

