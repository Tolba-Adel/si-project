# Generated by Django 5.0 on 2024-01-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_paiementcredit_montantpaiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiementcredit',
            name='montantPaiement',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
