from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.urls import reverse
from .models import * 
import json
from django.db import connection
import locale
"""def test(request):
        nom_user = request.session.get('nom_user')
        with open('C:\\Users\\halla\\OneDrive\\Bureau\\gestaweb\\gesta\\gestaapp\\script.sql', 'r') as sql_file:
            script = sql_file.read()

        with connection.cursor() as cursor:
            cursor.execute(script)
            results = cursor.fetchall()
            filtered_results=[]
            for res in results:
                if res[25]==nom_user:
                    filtered_results.append(res)
            info_list = []


            for item in filtered_results:
                first_info = item[0]  
                last_info = item[-1]  

                
                info_list.append({'num_facture':first_info,'user':last_info})
        return render(request, 'test1.html',{'results':info_list})
"""
"""import calendar
def test(request):
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    nom_user = request.session.get('nom_user')
    with open('C:\\Users\\halla\\OneDrive\\Bureau\\gestaweb\\gesta\\gestaapp\\script.sql', 'r') as sql_file:
        script = sql_file.read()

    with connection.cursor() as cursor:
        cursor.execute(script)
        results = cursor.fetchall()

    # Filtrer les résultats par nom d'utilisateur
    filtered_results = [res for res in results if res[25] == nom_user]

    # Préparer les données pour le graphique à barres
    data_dict = {}  # Dictionnaire pour stocker les données agrégées par mois

    for res in filtered_results:
        # Obtenir le mois et l'année au format 'm/a' pour utiliser comme clé du dictionnaire
        month_year = res[2].strftime('%m/%Y')

        # Si le mois existe déjà dans le dictionnaire, ajouter la valeur à la valeur existante
        if month_year in data_dict:
            data_dict[month_year] += 1
        # Sinon, créer une nouvelle entrée pour ce mois dans le dictionnaire
        else:
            data_dict[month_year] = 1

    # Convertir le dictionnaire en listes de labels et de valeurs pour le graphique à barres
    data_labels = []  # Liste des noms des mois
    data_values = []  # Liste des valeurs agrégées par mois

    for month_year in data_dict.keys():
        month, year = map(int, month_year.split('/'))
        month_name = calendar.month_name[month]  # Obtenir le nom du mois en utilisant la bibliothèque calendar
        data_labels.append(month_name+" "+str(year))
        data_values.append(data_dict[month_year])

    # Convertir les listes en chaînes JSON
    data_labels_json = json.dumps(data_labels)
    data_values_json = json.dumps(data_values)

    return render(request, 'test1.html', {'data_labels_json': data_labels_json, 'data_values_json': data_values_json,'data_labels':data_labels,'data_values':data_values,'user':nom_user})
"""
import calendar
import fdb
def test(request):
    

    nom_user = request.session.get('nom_user')
    connn = fdb.connect(
    host='192.168.11.145',  # L'adresse du serveur Firebird
    database='C:\GestionUSC\\2012\\USC\\Facturation\\CITYSHOPWIN\\DBCITYSHOP.FDB',  # Le chemin vers votre base de données
    user='SYSDBA',  # Le nom d'utilisateur
    password='15031973' # Le mot de passe
    
)
    cursor=connn.cursor()
    """fournisseurs"""
    cursor.execute("SELECT COUNT(code) AS NBR FROM F_FOURNISSEURS WHERE code > 1")
    result = cursor.fetchone()
    total_fournisseur=result[0]
    cursor.execute( "SELECT cast(COALESCE(SUM(Credit), 0) as dmonnaie ) AS Tcredit, COALESCE(SUM(Debit), 0) AS Tdebit, (COALESCE(SUM(Credit), 0) + COALESCE(SUM(Debit), 0)) AS SOLD FROM GLFOURNISSEUR WHERE fournisseur > 1")
    result = cursor.fetchone()
    soldes_fournisseur=int(result[0])
    cursor.execute("SELECT COUNT(rang) AS nbr, SUM(COALESCE(montant, 0) - COALESCE(REMISE, 0)) AS total FROM MOUVEMENT WHERE TYPE_MOUVE = 0")
    result = cursor.fetchone()
    entrees_fournisseur=result
    """produit"""
    cursor.execute("SELECT COUNT(A.Reference) AS NBR, COALESCE(SUM(COALESCE(S.qtephy, 0) * COALESCE(A.prix_achat, 0)), 0) AS stockinit, COALESCE(SUM(COALESCE(S.qte, 0) * COALESCE(A.prix_achat, 0)), 0) AS Totalstock FROM article A, stockglobale S WHERE S.reference = A.reference AND A.reference <> 0")
    result=cursor.fetchone()
    produit=result
    cursor.execute("SELECT COALESCE(SUM(COALESCE(S.qte, 0) * COALESCE(A.prix_achat, 0)), 0) AS totalstock FROM article A, stockglobale S WHERE S.reference = A.reference AND A.reference <> 0 AND S.qte < 0")
    result=cursor.fetchone()
    produit_stock_negatif=result[0]
    cursor.execute("SELECT COALESCE(AVG(marge), 0) AS marge FROM article")
    result=cursor.fetchone()
    marge_moy=result
    cursor.execute("select count(A.Reference) as NBR from article A, stockglobale S where s.reference = A.reference and A.reference <> 0 and cuisson = 1")
    result=cursor.fetchone()
    dont_fidelisee=result
    cursor.execute("select count(A.Reference) as NBR from article A, stockglobale S where s.reference = A.reference and A.reference <> 0 and porigine = 1")
    result=cursor.fetchone()
    dont_actif=result
    cursor.execute("select count(article) as nbr, sum(TOTALTTC) as total from ETAT_RETOUR_FOURNISSEURS")
    result=cursor.fetchone()
    retour_fournisseur=result[0]
    """client"""
    cursor.execute("select count(code) as NBR from Clients WHERE CODE > 0")
    result=cursor.fetchone()
    total_client=result[0]
    cursor.execute("select count(code) as NBR from Clients where fidelite = 1")
    result=cursor.fetchone()
    total_client_fideles=result[0]
    cursor.execute("select coalesce(sum(Credit), 0) as Tcredit, coalesce(sum(Debit), 0) as Tdebit, (coalesce(sum(Credit), 0) + coalesce(sum(Debit), 0)) as SOLD from GL where client > 0")
    result=cursor.fetchone()
    solde_client=result[0]
    cursor.execute("SELECT coalesce(SUM(F.valeur_plus), 0) AS valeur FROM valeur_fidelite_archive F")
    result=cursor.fetchone()
    valeur_fidelite=result[0]
    cursor.execute("select CAANNEE,MOISENCOUR from caannee")
    result=cursor.fetchall()
    ccanne=result
    data_dict = {}  # Dictionnaire pour stocker les données agrégées par mois

    for res in ccanne:
        # Obtenir le mois et l'année au format 'm/a' pour utiliser comme clé du dictionnaire
        month = res[1]

        # Si le mois existe déjà dans le dictionnaire, ajouter la valeur à la valeur existante
        
        data_dict[month] =res[0]
        # Sinon, créer une nouvelle entrée pour ce mois dans le dictionnaire
        

    # Convertir le dictionnaire en listes de labels et de valeurs pour le graphique à barres
    data_labels = []  # Liste des noms des mois
    data_values = []  # Liste des valeurs agrégées par mois

    for month in data_dict.keys():
        
         # Obtenir le nom du mois en utilisant la bibliothèque calendar
        data_labels.append(month)
        data_values.append(data_dict[month])

    # Convertir les listes en chaînes JSON
    data_labels_json = json.dumps(data_labels)
    data_values_json = json.dumps(data_values)
    
# row contient le résultat de la requête
    
    context = {
        'user':nom_user,
        'total_fournisseur':total_fournisseur,
        'soldes_fournisseur':soldes_fournisseur,
        'entrees_fournisseur':entrees_fournisseur[0],
        'entrees_fournisseur_somme':entrees_fournisseur[1],
        'nombre_produit':produit[0],
        'stock_initial':produit[1],
        'stock_total':produit[2],
        'produit_stock_negatif':produit_stock_negatif,
        'marge_moy':marge_moy[0],
        'dont_fidelisee':dont_fidelisee[0],
        'dont_actif':dont_actif[0],
        'retour_fournisseur':retour_fournisseur,
        'total_client':total_client,
        'total_client_fideles':total_client_fideles,
        'solde_client':solde_client,
        'valeur_fidelite':valeur_fidelite,
        'ccanne':ccanne,
        'data_labels_json': data_labels_json, 
        'data_values_json': data_values_json,
         
        }
    return render(request,'test1.html',context)



def dashboard(request):
    return render(request,"layouts/base.html")


def login_user(request):
    
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('test1')
        
        else:
            messages.success(request,("*Le nom d'utilisateur ou le mot de passe est incorrect. Veuillez réessayer.*"))
            return redirect('login')
    else:
        return render(request,'login.html')
    
def check_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = users_gesta.objects.get(nom_user=username)
            request.session['nom_user'] = username
            if (password.startswith('-') and password[1:].isdigit()) or password.isdigit():
                if user.passe == int(password):
                    
                    return redirect('test1') 
                    
                else:
                    error_message = 'User ou Mot de passe incorrect.'
                    messages.success(request, error_message)
                    return redirect('login')
            else:
                error_message = 'pwd is crypted.'
                messages.success(request, error_message)
                return redirect('login')
        
        except users_gesta.DoesNotExist:
            error_message = 'User ou Mot de passe incorrect.'
            messages.success(request, error_message)
            return redirect('login')
            
    else:
        return render(request, 'login.html')