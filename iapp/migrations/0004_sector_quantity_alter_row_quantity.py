# Generated by Django 4.1.7 on 2023-03-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0003_row_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='quantity',
            field=models.PositiveIntegerField(default=1, help_text='Qator sonini kiriting', verbose_name='Qatorlar soni'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='row',
            name='quantity',
            field=models.PositiveIntegerField(help_text='Joylar sonini kiriting', verbose_name='Joylar soni'),
        ),
    ]
