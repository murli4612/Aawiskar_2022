# Generated by Django 3.1.5 on 2022-05-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jai_Kisan', '0002_auto_20220516_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='productimg'),
        ),
    ]