# Generated by Django 3.1.14 on 2023-11-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_auto_20231129_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'), ('SNACKS', 'SNACKS')], max_length=200, null=True),
        ),
    ]
