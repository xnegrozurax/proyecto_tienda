# Generated by Django 4.0.4 on 2022-05-15 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items_Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('precio_producto', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='items_carrito')),
            ],
            options={
                'db_table': 'db_carriopro',
            },
        ),
        migrations.AlterModelTable(
            name='suscripcion',
            table='db_suscripcion',
        ),
    ]