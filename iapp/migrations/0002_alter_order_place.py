# Generated by Django 4.1.7 on 2023-03-17 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iapp.place', verbose_name='Joy'),
        ),
    ]
