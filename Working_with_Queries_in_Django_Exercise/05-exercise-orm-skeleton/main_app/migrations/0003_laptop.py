# Generated by Django 4.2.6 on 2023-11-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artworkgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')])),
                ('processor', models.CharField(max_length=100)),
                ('memory', models.PositiveIntegerField(help_text='Memory in GB')),
                ('storage', models.PositiveIntegerField(help_text='Storage in GB')),
                ('operation_system', models.CharField(choices=[('Windows', 'Windows'), ('Linux', 'Linux'), ('Mac OS', 'Mac OS'), ('Chrome OS', 'Chrome OS')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
