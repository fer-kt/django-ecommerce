# Generated by Django 3.2.4 on 2021-06-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TIENDA', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='imagenes'),
        ),
    ]