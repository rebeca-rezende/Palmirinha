# Generated by Django 4.2.7 on 2023-11-08 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='ingretientes',
            new_name='ingredientes',
        ),
    ]
