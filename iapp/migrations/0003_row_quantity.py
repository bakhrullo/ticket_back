# Generated by Django 4.1.7 on 2023-03-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0002_alter_order_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='quantity',
            field=models.PositiveIntegerField(default=1, help_text='Qator sonini kiriting', verbose_name='Qatorlar soni'),
            preserve_default=False,
        ),
    ]