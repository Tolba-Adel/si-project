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
    #Matiere Premiere
    path('matierePremiere',views.afficher_matierePremieres,name='liste_matierePremieres'),
    path('matierePremiere/edit/<int:pk>/',views.modifier_matierePremiere, name="editMP"),
    path('matierePremiere/delete/<int:pk>',views.supprimer_matierePremiere, name="deleteMP"),
    #Achat Matiere Premiere
    path('AchatMatierePremiere',views.Achat_matierePremiere, name="addMP"),
    path('JournalAchatMatierePremiere',views.afficher_JournalAchatMP,name="liste_AchatmatierePremieres"),
    path('JournalAchatMatierePremiere/edit/<int:pk>/',views.modifier_AchatmatierePremiere, name="editAchatMP"),
    path('JournalAchatMatierePremiere/delete/<int:pk>',views.supprimer_AchatmatierePremiere, name="deleteAchatMP"),
    path('ReglementFournisseur',views.ReglementAchat_matierePremiere,name="ReglerAchatMP"),
    path('get_solde/', views.get_solde, name='get_solde'),
    #Transfert Matiere Premiere
    path('TransfertMatierePremiere',views.Transfert_matierePremiere, name="TransMP"),
    path('JournalTransfertMatierePremiere',views.afficher_JournalTransfertMP, name="liste_TransfertmatierePremieres"),
    #Vente Matiere Premiere
    path('VenteMatierePremiere',views.Vente_MatierePremiere, name="VenteMP"),
    path('JournalVenteMatierePremiere',views.afficher_JournalVenteMP, name="liste_VentematierePremieres"),
    path('JournalVenteMatierePremiere/edit/<int:pk>/',views.modifier_VentematierePremiere, name="editVenteMP"),
    path('JournalVenteMatierePremiere/delete/<int:pk>',views.supprimer_VentematierePremiere, name="deleteVenteMP"),
    path('PaiementCredit',views.PaiementCredit_matierePremiere,name="PaiementCredMP"),
    path('get_credit/', views.get_credit, name='get_credit'),
    #Etat De Stock
    path('EtatDeStock',views.afficher_etatStock, name="EtatSock"),
    #Centre Section
    path('sectionCentre/<int:centre_id>',views.section_centre,name="section_centre"),
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


]
