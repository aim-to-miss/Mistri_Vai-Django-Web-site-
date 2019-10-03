# Generated by Django 2.2.2 on 2019-06-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homestat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_customer', models.TextField()),
                ('number_of_worker', models.TextField()),
                ('number_of_supplier', models.TextField()),
                ('slug', models.SlugField(default='homestat')),
            ],
        ),
    ]
