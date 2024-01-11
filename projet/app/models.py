from django.db import models
from datetime import datetime
import calculation



class client(models.Model):
    # codeCl=models.AutoField(primary_key=True)
    nomCl=models.CharField(max_length=50)
    prenomCl=models.CharField(max_length=50)
    adresseCl=models.CharField(max_length=50)
    telephoneCl=models.CharField(max_length=10)
    credit=models.FloatField(max_length=10)
    def __str__(self):
        return f"{self.nomCl} {self.prenomCl}"

class fournisseur(models.Model):
    # codeF=models.AutoField(primary_key=True)
    nomF=models.CharField(max_length=50)
    prenomF=models.CharField(max_length=50)
    adresseF=models.CharField(max_length=50)
    telephoneF=models.CharField(max_length=10)
    solde=models.FloatField(max_length=10)
    def __str__(self):
        return f"{self.nomF} {self.prenomF}"

centre_possibles=[
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]
class centre(models.Model):
    # codeC=models.AutoField(primary_key=True)
    nomC=models.CharField(max_length=50)
    numeroC=models.IntegerField(choices=centre_possibles,unique=True)
    # responsable=models.ForeignKey(employe,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.numeroC}"
    
class employe(models.Model):
    # codeE=models.AutoField(primary_key=True)
    nomE=models.CharField(max_length=50)
    prenomE=models.CharField(max_length=50)
    adresseE=models.CharField(max_length=50)
    telephoneE=models.CharField(max_length=10)
    salaire_jour=models.FloatField(max_length=10)
    centre=models.ForeignKey(centre,on_delete=models.SET_NULL,null=True)
    points=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.nomE} {self.prenomE}"

# class pointage(models.Model):
#     employe=models.OneToOneField(employe,on_delete=models.CASCADE,unique=True)
#     points=models.IntegerField(default=0)
#     def __str__(self):
#         return f"{self.employe} - {self.points}"
    
class absence(models.Model):
    employe=models.ForeignKey(employe,on_delete=models.CASCADE)
    dateAbsence=models.DateField()
    def __str__(self):
        return f"{self.employe} - {self.dateAbsence}"

class avanceSalaire(models.Model):
    employe=models.ForeignKey(employe,on_delete=models.CASCADE)
    montant=models.FloatField()
    dateDemande=models.DateField()
    def __str__(self):
        return f"{self.employe} - {self.dateDemande}"

class produit(models.Model):
    # codeP=models.AutoField(primary_key=True)
    nomP=models.CharField(max_length=50)
    prix_achat=models.FloatField(max_length=10)
    prix_vente=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomP

class matierePremiere(models.Model):
    # codeM=models.AutoField(primary_key=True)
    nomMP=models.CharField(max_length=50)
    TypeMP=models.CharField(max_length=50)
    Quantite=models.IntegerField()
    Fournisseur=models.ForeignKey(fournisseur,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.nomMP

class achat(models.Model):
    # NumAchat=models.AutoField(primary_key=True,default=1)
    dateAchat=models.DateTimeField(default=datetime.now)
    fournisseur=models.ForeignKey(fournisseur,null=True,on_delete=models.CASCADE)
    matieresAchetes=models.ForeignKey(matierePremiere,null=True,on_delete=models.CASCADE)
    QteAchat=models.IntegerField(default=0)
    prixAchat=models.FloatField(default=0)
    montantTotal=models.FloatField(default=0)
    montantverse=models.FloatField(default=0)
    montantRestant=models.FloatField(default=0)
    def __str__(self):
        return f"{self.matieresAchetes}"

class ReglementFournisseur(models.Model):
    dateReg=models.DateTimeField(default=datetime.now)
    Fournisseur=models.ForeignKey(fournisseur,on_delete=models.CASCADE,default=1)
    solde=models.FloatField(default=0)
    montantReg=models.FloatField(default=0)
    def __str__(self):
        return f"Reglement fournisseur: {self.Fournisseur}"


class TransfertMatierePremiere(models.Model):
    # codeTransfert=models.AutoField(primary_key=True)
    dateTransfert=models.DateTimeField(default=datetime.now)
    centre=models.ForeignKey(centre, on_delete=models.CASCADE)
    MatieresTransferes=models.ForeignKey(achat, on_delete=models.CASCADE)
    QteTrf=models.IntegerField()
    PrixUTA=models.FloatField(default=0)
    CoutTrf=models.IntegerField(default=0) 
    def __str__(self):
        return f"Transfert #{self.id}"



class VenteMatierePremiere(models.Model):
    # codeVenteMP=models.AutoField(primary_key=True)
    dateVente=models.DateTimeField(default=datetime.now)
    client=models.ForeignKey(client,null=True,on_delete=models.CASCADE)
    MPVendus=models.ForeignKey(matierePremiere,null=True,on_delete=models.CASCADE)
    QteVds=models.IntegerField(default=0)
    prixUT=models.FloatField(default=0)
    montantVente=models.FloatField(default=0)
    montantEncaisse=models.FloatField(default=0)
    ResteAPayer=models.FloatField(default=0)
    def __str__(self):
        return f"{self. MPVendus}"