# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class users_gesta(models.Model):
    nom_user = models.CharField(unique=True, max_length=20, blank=True, null=True)
    fonction = models.CharField(max_length=20, blank=True, null=True)
    passe = models.IntegerField(blank=True, null=True)
    droit = models.CharField(max_length=80, blank=True, null=True)
    code = models.CharField(primary_key=True, max_length=20)
    typeuser = models.SmallIntegerField(blank=True, null=True)
    hstart = models.TimeField(blank=True, null=True)
    hclose = models.TimeField(blank=True, null=True)
    idcarte = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'gestaapp'


class Customuser(models.Model):

   usr=models.CharField(max_length=100,default=None)
   pwd=models.CharField(max_length=50,default=None)


class Persons(models.Model):
    personid = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons' #ue à Django de ne pas gérer les opérations de migration pour cette table
        app_label = 'gestaapp'  # Re


class JourneeCaisseBack(models.Model):
    n_journee = models.IntegerField(primary_key=True)
    date_ouvert = models.DateField(blank=True, null=True)
    date_cloture = models.DateField(blank=True, null=True)
    ouvertepar = models.CharField(max_length=20, blank=True, null=True)
    cloturepar = models.CharField(max_length=20, blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    fond_caisse_ouvert = models.FloatField(blank=True, null=True)
    fond_caisse_suivant = models.FloatField(blank=True, null=True)
    entree_caisse = models.FloatField(blank=True, null=True)
    sortie_caisse = models.FloatField(blank=True, null=True)
    retrait_caisse = models.FloatField(blank=True, null=True)
    cloture = models.SmallIntegerField(blank=True, null=True)
    caisse = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    total_benefice = models.FloatField(blank=True, null=True)
    ecart = models.FloatField(blank=True, null=True)
    total_recup = models.FloatField(blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journee_caisse_back'
        app_label = 'gestaapp'

class TComptoirPBack(models.Model):
    n_facture = models.IntegerField(primary_key=True)
    montant = models.FloatField(blank=True, null=True)
    valide = models.SmallIntegerField(blank=True, null=True)
    journee = models.DateField(blank=True, null=True)
    fondcaisse = models.FloatField(blank=True, null=True)
    caisse = models.IntegerField(blank=True, null=True)
    client = models.IntegerField(blank=True, null=True)
    num_journee = models.ForeignKey(JourneeCaisseBack, models.DO_NOTHING, db_column='num_journee', blank=True, null=True)
    num_table = models.FloatField(blank=True, null=True)
    num_payement = models.IntegerField(blank=True, null=True)
    creepar = models.CharField(max_length=20, blank=True, null=True)
    validepar = models.CharField(max_length=20, blank=True, null=True)
    mode = models.SmallIntegerField(blank=True, null=True)
    montant_w = models.FloatField(blank=True, null=True)
    montant_tva = models.FloatField(blank=True, null=True)
    m_tmbre = models.FloatField(blank=True, null=True)
    type_versement = models.CharField(max_length=20, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    lclient = models.CharField(max_length=60, blank=True, null=True)
    vendeur = models.DateTimeField(blank=True, null=True)
    facture = models.IntegerField(blank=True, null=True)
    detailpartennaire = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_comptoir_p_back'
        app_label = 'gestaapp'


    