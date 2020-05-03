# Generated by Django 2.2 on 2020-04-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialdistancing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_type',
            field=models.CharField(choices=[('Grocery', 'Grocery'), ('Medical-Store', 'Medical-Store'), ('Food', 'Food')], default='Grocery', max_length=245),
        ),
    ]