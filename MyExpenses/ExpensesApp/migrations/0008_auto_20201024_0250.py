# Generated by Django 3.1.2 on 2020-10-23 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpensesApp', '0007_auto_20201024_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ExpensesApp.profile'),
        ),
    ]