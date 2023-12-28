from django.db import models
from datetime import datetime

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

class centre(models.Model):
    centre_possibles=[
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]
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
    prix_achatMP=models.FloatField(max_length=10)
    prix_venteMP=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomMP

# class vente(models.Model):
#     # codeVente=models.AutoField(primary_key=True)
#     dateVente=models.DateTimeField(default=datetime.now)
#     client=models.ForeignKey(client,on_delete=models.CASCADE)
#     produitsVendus=models.ManyToManyField(produit,related_name="vente")
    
# class achat(models.Model):
#     # codeAchat=models.AutoField(primary_key=True)
#     dateAchat=models.DateTimeField(default=datetime.now)
#     produitsAchetes=models.ManyToManyField(produit,related_name="achat")
#     fournisseur=models.ForeignKey(fournisseur,on_delete=models.CASCADE)
    
# class transfert(models.Model):
#     # codeTransfert=models.AutoField(primary_key=True)
#     dateTransfert=models.DateTimeField(default=datetime.now)
#     produitsTransferes=models.ManyToManyField(produit,related_name="transfert")
#     centre=models.ForeignKey(centre,on_delete=models.CASCADE)

