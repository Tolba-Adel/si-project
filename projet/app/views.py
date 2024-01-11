from django.shortcuts import render,redirect,get_object_or_404
from .models import fournisseur,client,employe,centre,matierePremiere,absence,avanceSalaire,achat,TransfertMatierePremiere,ReglementFournisseur,VenteMatierePremiere
from .forms import clientForm,fournisseurForm,employeForm,centreForm,matierePremiereForm,AchatmatierePremiereForm,TransfertmatierePremiereForm,ReglementMPForm,VentematierePremiereForm

#Home Page
def index(request):
    return render(request,"index.html")
def magasin(request):
    return render(request,"index/Magasin.html")
def centres(request):
    return render(request,"index/Centres.html")
def tableauxDeBord(request):
    return render(request,"index/TableauxDeBord.html")


#Magasin Section
#Gestion Client
def afficher_clients(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            clients=client.objects.filter(nomCl__icontains=query)
        else:
            clients = client.objects.all()
        return render(request,"magasin/client/client.html",{'clients':clients})

def ajouter_client(request):
    if request.method == "POST":
        form=clientForm(request.POST)
        if form.is_valid():
            form.save()
            form=clientForm()
            msg="Client ajoutée avec succès"
            return render(request,"magasin/client/addClient.html",{'form':form,"message":msg})
    else:
        form=clientForm() # créer une instance de formulaire vierge
        msg=""
        return render(request,"magasin/client/addClient.html",{"form":form,"message":msg})

def modifier_client(request,pk):
    cl=client.objects.get(id=pk)
    if request.method == "POST":
        form=clientForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return redirect("liste_clients")
    else:
        form=clientForm(instance=cl)
        return render(request,"magasin/client/editClient.html",{"form":form})

def supprimer_client(request,pk):
    cl = get_object_or_404(client,id=pk)
    if request.method == 'POST':
        cl.delete() 
        return redirect('liste_clients')
    # Si la requête est une GET, afficher la page de confirmation de suppression
    return render(request, 'magasin/client/confirmDelete.html', {'client': cl})


#Gestion Fournisseur
def afficher_fournisseurs(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            fournisseurs=fournisseur.objects.filter(nomF__icontains=query)
        else:
            fournisseurs=fournisseur.objects.all()
        return render(request,"magasin/fournisseur/fournisseur.html",{'fournisseurs':fournisseurs})

def ajouter_fournisseur(request):
    if request.method == "POST":
        form=fournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form=fournisseurForm()
            msg="Fournisseur ajoutée avec succès"
            return render(request,"magasin/fournisseur/addFournisseur.html",{'form':form,"message":msg})
    else:
        form=fournisseurForm()
        msg=""
        return render(request,"magasin/fournisseur/addFournisseur.html",{"form":form,"message":msg})

def modifier_fournisseur(request,pk):
    f=fournisseur.objects.get(id=pk)
    if request.method == "POST":
        form=fournisseurForm(request.POST,instance=f)
        if form.is_valid():
            form.save()
            return redirect("liste_fournisseurs")
    else:
        form=fournisseurForm(instance=f)
        return render(request,"magasin/fournisseur/editFournisseur.html",{"form":form})

def supprimer_fournisseur(request,pk):
    f=get_object_or_404(fournisseur,id=pk)
    if request.method == 'POST':
        f.delete() 
        return redirect('liste_fournisseurs')
    return render(request,'magasin/fournisseur/confirmDelete.html',{'fournisseur': f})


#Gestion Employe
def afficher_employes(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            employes=employe.objects.filter(nomE__icontains=query)
        else:
            employes=employe.objects.all()
        return render(request,"magasin/employe/employe.html",{'employes':employes})

def ajouter_employe(request):
    if request.method == "POST":
        form=employeForm(request.POST)
        if form.is_valid():
            form.save()
            form=employeForm()
            msg="Employe ajoutée avec succès"
            return render(request,"magasin/employe/addEmploye.html",{'form':form,"message":msg})
    else:
        form=employeForm()
        msg=""
        return render(request,"magasin/employe/addEmploye.html",{"form":form,"message":msg})

def modifier_employe(request,pk):
    e=employe.objects.get(id=pk)
    if request.method == "POST":
        form=employeForm(request.POST,instance=e)
        if form.is_valid():
            form.save()
            return redirect("liste_employes")
    else:
        form=employeForm(instance=e)
        return render(request,"magasin/employe/editEmploye.html",{"form":form})

def supprimer_employe(request,pk):
    e=get_object_or_404(employe,id=pk)
    if request.method == 'POST':
        e.delete() 
        return redirect('liste_employes')
    return render(request,'magasin/employe/confirmDelete.html',{'employe':e})


#Gestion Centre
def afficher_centres(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            centres=centre.objects.filter(nomC__icontains=query)
        else:
            centres = centre.objects.all()
        return render(request,"magasin/centre/centre.html",{'centres':centres})

def ajouter_centre(request):
    if request.method == "POST":
        form=centreForm(request.POST)
        if form.is_valid():
            form.save()
            form=centreForm()
            msg="Centre ajoutée avec succès"
        else:
            form=centreForm()
            msg="Numéro du Centre deja existant"
    else:
        form=centreForm()
        msg=""
    return render(request,"magasin/centre/addCentre.html",{"form":form,"message":msg})

def modifier_centre(request,pk):
    c=centre.objects.get(id=pk)
    if request.method == "POST":
        form=centreForm(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return redirect("liste_centres")
        else:
            form=centreForm(instance=c)
            msg="Numéro du Centre deja existant"
            return render(request,"magasin/centre/editCentre.html",{"form":form,"message":msg})

    else:
        form=centreForm(instance=c)
        return render(request,"magasin/centre/editCentre.html",{"form":form})

def supprimer_centre(request,pk):
    c=get_object_or_404(centre,id=pk)
    if request.method == 'POST':
        c.delete() 
        return redirect('liste_centres')
    return render(request,'magasin/centre/confirmDelete.html',{'centre':c})


#Gestion Matiere Premiere

def afficher_matierePremieres(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            matierePremieres=matierePremiere.objects.filter(nomMP__icontains=query)
        else:
            matierePremieres=matierePremiere.objects.all()
        return render(request,"magasin/matierePremiere/matierePremiere.html",{'matierePremieres':matierePremieres})

def modifier_matierePremiere(request,pk):
    mp=matierePremiere.objects.get(id=pk)
    if request.method == "POST":
        form=matierePremiereForm(request.POST,instance=mp)
        if form.is_valid():
            form.save()
            return redirect("liste_matierePremieres")
    else:
        form=matierePremiereForm(instance=mp)
        return render(request,"magasin/matierePremiere/editMatierePremiere.html",{"form":form})

def supprimer_matierePremiere(request,pk):
    mp=get_object_or_404(matierePremiere,id=pk)
    if request.method == 'POST':
        mp.delete() 
        return redirect('liste_matierePremieres')
    return render(request,'magasin/matierePremiere/confirmDelete.html',{'matierePremiere':mp})


#Achat matiere premiere

def Achat_matierePremiere(request):
    if request.method == "POST":
        form=AchatmatierePremiereForm(request.POST)
        print(form['matieresAchetes'].value()[0])
        if form.is_valid():
            selectedMP = matierePremiere.objects.get(pk=form['matieresAchetes'].value()[0])
            selectedMP.Quantite = selectedMP.Quantite + int(form['QteAchat'].value())
            selectedMP.save()
            solFour = fournisseur.objects.get(pk=form['fournisseur'].value()[0])
            solFour.solde=solFour.solde + int(form['montantRestant'].value())
            solFour.save()
            form.save()
            form=AchatmatierePremiereForm()
            msg="Achat Matière Première avec succès"
            return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{'form':form,"message":""})
    else:
        form=AchatmatierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{"form":form,"message":msg})

def ReglementAchat_matierePremiere(request):
    if request.method == "POST":
        form=ReglementMPForm(request.POST)
        if form.is_valid():
            # selectedF = form.save(commit = False)
            # selectedF.solde = fournisseur.objects.get(pk=form['solde'].value()[0]).solde
            # selectedF.save()
            editSoldeF = achat.objects.get(pk=form['Fournisseur'].value()[0])
            editSoldeF.montantRestant = editSoldeF.montantRestant - float(form['montantReg'].value())
            editSoldeF.save()
            form.save()
            form=ReglementMPForm()
            msg="Reglement solde fournisseur avec succès"
            return render(request,"magasin/matierePremiere/ReglementAchat.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/ReglementAchat.html",{'form':form,"message":""})
    else:
        form=ReglementMPForm()
        msg=""
        return render(request,"magasin/matierePremiere/ReglementAchat.html",{"form":form,"message":msg})

# Journal Achat Matiere Premiere

def afficher_JournalAchatMP(request):
      if request.method == "GET":
          query = request.GET.get('recherche')
          sort_by = request.GET.get('sort_by', 'dateAchat')
          if query:
              achatmatierePremieres=achat.objects.filter(matieresAchetes__nomMP__icontains=query).order_by(sort_by)
          else:
              achatmatierePremieres=achat.objects.all().order_by(sort_by)

          return render(request,'magasin/matierePremiere/JournalAchatMP.html',{"achatmatierePremieres":achatmatierePremieres})
  
def modifier_AchatmatierePremiere(request,pk):
    mp=achat.objects.get(id=pk)
    if request.method == "POST":
        form=AchatmatierePremiereForm(request.POST,instance=mp)
        if form.is_valid():
            form.save()
            return redirect("liste_AchatmatierePremieres")
    else:
        form=AchatmatierePremiereForm(instance=mp)
        return render(request,"magasin/matierePremiere/EditAchatMatierePremiere.html",{"form":form})

def supprimer_AchatmatierePremiere(request,pk):
    mp=get_object_or_404(achat,id=pk)
    if request.method == 'POST':
            form=AchatmatierePremiereForm(request.POST)
            selectedMP = matierePremiere.objects.get(pk=mp.matieresAchetes.all()[0].id)
            selectedMP.Quantite = selectedMP.Quantite - int(mp.QteAchat)
            selectedMP.save()
            mp.delete() 
            return redirect('liste_AchatmatierePremieres')
    return render(request,'magasin/matierePremiere/DelAchatMatierePremiere.html',{'matierePremiere':mp})

# Transfert Matiere Premiere  

def Transfert_matierePremiere(request):
    
    if request.method == "POST":
        form=TransfertmatierePremiereForm(request.POST)
        print(form['MatieresTransferes'].value()[0])
        if form.is_valid():
            editForm = form.save(commit = False)
            editForm.PrixUTA = achat.objects.get(pk=form['MatieresTransferes'].value()[0]).prixAchat

            editForm.CoutTrf = achat.objects.get(pk=form['MatieresTransferes'].value()[0]).prixAchat * int(form['QteTrf'].value())
            
            editForm.save()
            selectedMP = matierePremiere.objects.get(pk=form['MatieresTransferes'].value()[0])
            selectedMP.Quantite = selectedMP.Quantite - int(form['QteTrf'].value())

            selectedMP.save()
            form=TransfertmatierePremiereForm()
            msg="Transfert Matière Première avec succès"
            return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{'form':form,"message":""})
    else:
        form=TransfertmatierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{"form":form,"message":msg})

# Journal de Transfert Matiere Premiere 
def afficher_JournalTransfertMP(request):
      if request.method == "GET":
          query = request.GET.get('recherche')
          sort_by = request.GET.get('sort_by', 'dateTransfert')
          if query:
              transfertmatierePremieres=TransfertMatierePremiere.objects.filter(MatieresTransferes__nomMP__icontains=query).order_by(sort_by)
          else:
              transfertmatierePremieres=TransfertMatierePremiere.objects.all().order_by(sort_by)

          return render(request,'magasin/matierePremiere/JournalTransfertMP.html',{"transfertmatierePremieres":transfertmatierePremieres})

# Vente Matiere Premiere

def Vente_MatierePremiere(request):
    if request.method == "POST":
        form=VentematierePremiereForm(request.POST)
        print(form['MPVendus'].value()[0])
        if form.is_valid():
            selectedMP = matierePremiere.objects.get(pk=form['MPVendus'].value()[0])
            selectedMP.Quantite = selectedMP.Quantite - int(form['QteVds'].value())
            selectedMP.save()
            credCL = client.objects.get(pk=form['client'].value()[0])
            credCL.credit=credCL.credit + int(form['ResteAPayer'].value())
            credCL.save()
            form.save()
            form=VentematierePremiereForm()
            msg="Vente Matière Première avec succès"
            return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{'form':form,"message":""})
    else:
        form=VentematierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{"form":form,"message":msg})

#Journal de Vente Matiere Premiere 
def afficher_JournalVenteMP(request):
      if request.method == "GET":
          query = request.GET.get('recherche')
          sort_by = request.GET.get('sort_by', 'dateVente')
          if query:
              ventematierePremieres=VenteMatierePremiere.objects.filter(MPVendus__nomMP__icontains=query).order_by(sort_by)
          else:
              ventematierePremieres=VenteMatierePremiere.objects.all().order_by(sort_by)

          return render(request,'magasin/matierePremiere/JournalVenteMP.html',{"ventematierePremieres":ventematierePremieres})

#Centre Section
def section_centre(request,centre_id):
    centre_id=centre_id
    return render(request,"centre/modules.html",{'centre_id':centre_id})
 
def module_employe(request,centre_id):
    c=centre.objects.get(numeroC=centre_id)
    employes=employe.objects.filter(centre=c)
    return render(request,"centre/moduleEmploye.html",{'centre_id':centre_id,'employes':employes})

#Syteme Pointage
def modifier_points(request,pk):
    msg=""
    e=employe.objects.get(id=pk)
    if request.method == "POST":
        new_points=request.POST.get("points")
        if new_points is not None and new_points.isdigit():
            e.points=int(new_points)
            e.save()
            return redirect("module_employe",centre_id=e.centre.numeroC)
        else:
            msg="Valeur de Points invalide"
            return render(request,"centre/editPoints.html",{"employe":e,"message":msg})
    else:
        return render(request,"centre/editPoints.html",{"employe":e,"message":msg})

#Systeme Absence
def afficher_absence(request,pk):
    e=employe.objects.get(id=pk)
    absences=absence.objects.filter(employe=pk)
    return render(request,"centre/absences.html",{'absences':absences,'employe':e})

def ajouter_absence(request,employe_id):
    msg=""
    if request.method == "POST":
        date_absence=request.POST.get("dateAbsence")
        e=employe.objects.get(id=employe_id)
        absence.objects.create(employe=e,dateAbsence=date_absence)
        msg="Absence ajoutée avec succès"
    return render(request,"centre/addAbsence.html",{'employe_id':employe_id,"message":msg})

def modifier_absence(request,pk):
    a=absence.objects.get(id=pk)
    if request.method == "POST":
        a.dateAbsence=request.POST.get("dateAbsence")
        a.save()
        return redirect("absence",pk=a.employe.id)
    else:
        date_absence=a.dateAbsence.strftime('%Y-%m-%d') #Format the date for display
        return render(request,"centre/editAbsence.html",{'absence':a,'dateAbsence':date_absence})

def supprimer_absence(request,pk):
    a=get_object_or_404(absence,id=pk)
    if request.method == 'POST':
        a.delete() 
        return redirect("absence",pk=a.employe.id)
    return render(request,'centre/deleteAbsence.html',{'absence':a})


#Systeme Avance Salaire
def afficher_avanceSalaire(request,pk):
    e=employe.objects.get(id=pk)
    avanceSalaires=avanceSalaire.objects.filter(employe=pk)
    return render(request,"centre/avanceSalaire.html",{'avanceSalaires':avanceSalaires,'employe':e})

def ajouter_avanceSalaire(request,employe_id):
    msg=""
    if request.method == 'POST':
        montant=request.POST.get('montant')
        date_avanceSalaire=request.POST.get('dateAvanceSalaire')
        e=employe.objects.get(id=employe_id)
        avanceSalaire.objects.create(employe=e,montant=montant,dateDemande=date_avanceSalaire)
        msg="Demande ajoutée avec succès"
    return render(request,"centre/addAvanceSalaire.html",{'employe_id':employe_id,"message":msg})

def modifier_avanceSalaire(request,pk):
    avanceS=avanceSalaire.objects.get(id=pk)
    if request.method == "POST":
        avanceS.montant=request.POST.get("montant")
        avanceS.dateDemande=request.POST.get("dateAvanceSalaire")
        avanceS.save()
        return redirect("avanceSalaire",pk=avanceS.employe.id)
    else:
        date_avanceSalaire=avanceS.dateDemande.strftime('%Y-%m-%d')
        return render(request,"centre/editAvanceSalaire.html",{'avanceSalaire':avanceS,'dateAvanceSalaire':date_avanceSalaire,'montant':avanceS.montant})

def supprimer_avanceSalaire(request,pk):
    avanceS=get_object_or_404(avanceSalaire,id=pk)
    if request.method == "POST":
        avanceS.delete()
        return redirect("avanceSalaire",pk=avanceS.employe.id)
    return render(request,"centre/delteAvanceSalaire.html",{'avanceSalaire':avanceS})





# def achatMatieres(request):
#     return render(request,"magasin/AchatMatieres.html")

# def getFournisseurs(request):
#     fournisseurs=fournisseur.objects.all()
#     return render(request,"AchatMatieres.html",{'fournisseurs':fournisseurs})