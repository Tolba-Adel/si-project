from django.urls import path
from . import views  

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),

    path('magasin',views.magasin, name='magasin'),
    path('centres',views.centres, name='centres'),
    path('tableauxDeBord',views.tableauxDeBord, name='TableauxDeBord'),

    # path('magasin/AchatMatieres',views.achatMatieres,name='achatMatieres'),

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
    path('centre/ajouter',views.ajouter_centre, name="addC"),
    path('centre/edit/<int:pk>',views.modifier_centre, name="editC"),
    path('centre/delete/<int:pk>',views.supprimer_centre, name="deleteC"),

    #Matiere Premiere
    path('matierePremiere',views.afficher_matierePremieres,name='liste_matierePremieres'),
    path('matierePremiere/ajouter',views.ajouter_matierePremiere, name="addMP"),
    path('matierePremiere/edit/<int:pk>',views.modifier_matierePremiere, name="editMP"),
    path('matierePremiere/delete/<int:pk>',views.supprimer_matierePremiere, name="deleteMP"),

]
