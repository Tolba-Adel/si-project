from django.urls import path
from . import views  

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),

    path('magasin',views.magasin, name='magasin'),
    path('centres',views.centres, name='centres'),
    path('tableauxDeBord',views.tableauxDeBord, name='TableauxDeBord'),


    #Magasin Section
    #Client
    path('client',views.afficher_clients,name='liste_clients'),
    path('client/ajouter',views.ajouter_client, name="addCl"),
    path('client/edit/<int:pk>',views.modifier_client, name="editCl"),
    path('client/delete/<int:pk>',views.supprimer_client, name="deleteCl"),
    #Fournisseur
    path('fournisseur',views.afficher_fournisseurs,name='liste_fournisseurs'),
    path('fournisseur/ajouter',views.ajouter_fournisseur, name="addF"),
    path('fournisseur/edit/<int:pk>',views.modifier_fournisseur, name="editF"),
    path('fournisseur/delete/<int:pk>',views.supprimer_fournisseur, name="deleteF"),
    #Employe
    path('employe',views.afficher_employes,name='liste_employes'),
    path('employe/ajouter',views.ajouter_employe, name="addE"),
    path('employe/edit/<int:pk>',views.modifier_employe, name="editE"),
    path('employe/delete/<int:pk>',views.supprimer_employe, name="deleteE"),
    #Centre
    path('centre',views.afficher_centres,name='liste_centres'),
    #Produit
    path('produit',views.afficher_produits,name='liste_produits'),
    path('produit/ajouter',views.ajouter_produit, name="addPrd"),
    path('produit/edit/<int:pk>',views.modifier_produit, name="editPrd"),
    path('produit/delete/<int:pk>',views.supprimer_produit, name="deletePrd"),


    #Centre Section
    path('sectionCentre/<int:centre_id>',views.section_centre,name="section_centre"),
    #Activités du Centre
    path('activitesCentre/<int:centre_id>',views.activites_centre,name="activites_centre"),
    #Journal des Transferts
    path('journalTransfert/<int:centre_id>',views.journal_transfert,name="journal_transfert"),
    #Ventes des Produits
    path('journalVente/<int:centre_id>',views.journal_vente,name="journal_vente"),
    path('journalVente/ajouter/<int:centre_id>',views.ajouter_vente,name="addVente"),
    #Paiement Crédit Client
    path('paiementCredit/<int:centre_id>',views.paiement_credit,name="paiement_credit"),

    #Module Employé
    path('moduleEmploye/<int:centre_id>',views.module_employe,name="module_employe"),
    path('modifierPoints/<int:pk>',views.modifier_points,name="editPts"),

    path('absence/<int:pk>',views.afficher_absence,name="absence"),
    path('absence/ajouter/<int:employe_id>',views.ajouter_absence,name="addAbsence"),
    path('absence/edit/<int:pk>',views.modifier_absence,name="editAbsence"),
    path('absence/delete/<int:pk>',views.supprimer_absence,name="deleteAbsence"),

    path('avanceSalaire/<int:pk>',views.afficher_avanceSalaire,name="avanceSalaire"),
    path('avanceSalaire/ajouter/<int:employe_id>',views.ajouter_avanceSalaire,name="addAvanceSalaire"),
    path('avanceSalaire/edit/<int:pk>',views.modifier_avanceSalaire,name="editavanceSalaire"),
    path('avanceSalaire/delete/<int:pk>',views.supprimer_avanceSalaire,name="deleteavanceSalaire"),


    #Tableux de Bord Section
    path('analyseVente',views.analyse_vente,name="analyse_vente"),
    path('tableauxDeBord/<int:centre_id>',views.afficher_tableaux,name="tableaux_de_bord"),

]
