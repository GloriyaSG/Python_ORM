# Generated by Django 4.2.6 on 2023-12-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')], max_length=30),
        ),
    ]
