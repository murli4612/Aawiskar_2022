# Generated by Django 3.1.5 on 2022-05-27 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jai_Kisan', '0005_farmer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Tracter', 'Tracter'), ('Boring Machine', 'Boring Machine'), ('Harvestor', 'Harvestor'), ('Cultivator', 'Cultivater')], max_length=20),
        ),
        migrations.CreateModel(
            name='VendorProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Tracter', 'Tracter'), ('Boring Machine', 'Boring Machine'), ('Harvestor', 'Harvestor'), ('Cultivator', 'Cultivater')], max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jai_Kisan.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
