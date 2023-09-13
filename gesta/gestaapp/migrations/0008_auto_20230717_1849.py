# Generated by Django 2.2.28 on 2023-07-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaapp', '0007_auto_20230717_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('nom_user', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('fonction', models.CharField(blank=True, max_length=20, null=True)),
                ('passe', models.IntegerField(blank=True, null=True)),
                ('droit', models.CharField(blank=True, max_length=80, null=True)),
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('typeuser', models.SmallIntegerField(blank=True, null=True)),
                ('hstart', models.TimeField(blank=True, null=True)),
                ('hclose', models.TimeField(blank=True, null=True)),
                ('idcarte', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'USERS',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Users_gesta',
        ),
    ]
