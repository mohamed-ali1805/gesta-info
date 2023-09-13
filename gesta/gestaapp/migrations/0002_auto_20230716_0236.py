# Generated by Django 2.2.28 on 2023-07-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='persons',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'persons',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Yadrahhhh',
        ),
    ]