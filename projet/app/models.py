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
    # codeC=models.AutoField(primary_key=True)
    nomC=models.CharField(max_length=50)
    # responsable=models.ForeignKey(employe,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.nomC
    
class employe(models.Model):
    # codeE=models.AutoField(primary_key=True)
    nomE=models.CharField(max_length=50)
    prenomE=models.CharField(max_length=50)
    adresseE=models.CharField(max_length=50)
    telephoneE=models.CharField(max_length=10)
    salaire_jour=models.FloatField(max_length=10)
    centre=models.ForeignKey(centre,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nomE} {self.prenomE}"

class produit(models.Model):
    # codeP=models.AutoField(primary_key=True)
    nomP=models.CharField(max_length=50)
    prix_achat=models.FloatField(max_length=10)
    prix_vente=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomP

class matierePremiere(models.Model):
    # codeM=models.AutoField(primary_key=True)
    nomM=models.CharField(max_length=50)
    prix_achatM=models.FloatField(max_length=10)
    prix_venteM=models.FloatField(max_length=10)
    def __str__(self):
        return self.nomM

# class achat(models.Model):
#     # codeAchat=models.AutoField(primary_key=True)
#     dateAchat=models.DateTimeField(default=datetime.now)
#     produitsAchete=models.ManyToManyField(produit,related_name="achat")
#     fournisseur=models.ForeignKey(fournisseur,ondelete=models.CASCADE)
    
# class vente(models.Model):
#     # codeVente=models.AutoField(primary_key=True)
#     dateVente=models.DateTimeField(default=datetime.now)
#     produitsVendu=models.ManyToManyField(produit,related_name="vente")
#     client=models.ForeignKey(client,ondelete=models.CASCADE)


# class transfert(models.Model):
#     # codeTransfert=models.AutoField(primary_key=True)
#     dateTransfert=models.DateTimeField(default=datetime.now)
#     produitsTransfere=models.ManyToManyField(produit,related_name="transfert")
#     centre=models.ForeignKey(centre,ondelete=models.CASCADE)

