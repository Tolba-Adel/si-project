from django.shortcuts import render,redirect,get_object_or_404
from .models import fournisseur,client,employe,centre,matierePremiere
from .forms import clientForm,fournisseurForm,employeForm,centreForm,matierePremiereForm

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
            msg="Client ajoutée avec succées"
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
            msg="Fournisseur ajoutée avec succées"
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
            msg="Employe ajoutée avec succées"
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
            msg="Centre ajoutée avec succées"
            return render(request,"magasin/centre/addCentre.html",{'form':form,"message":msg})
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

def ajouter_matierePremiere(request):
    if request.method == "POST":
        form=matierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            form=matierePremiereForm()
            msg="Matière Première ajoutée avec succées"
            return render(request,"magasin/matierePremiere/addMatierePremiere.html",{'form':form,"message":msg})
    else:
        form=matierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/addMatierePremiere.html",{"form":form,"message":msg})

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






# def achatMatieres(request):
#     return render(request,"magasin/AchatMatieres.html")

# def getFournisseurs(request):
#     fournisseurs=fournisseur.objects.all()
#     return render(request,"AchatMatieres.html",{'fournisseurs':fournisseurs})