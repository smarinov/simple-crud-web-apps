# Generated by Django 3.1.2 on 2020-10-24 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpensesApp', '0010_auto_20201024_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpensesApp.profile'),
        ),
    ]
