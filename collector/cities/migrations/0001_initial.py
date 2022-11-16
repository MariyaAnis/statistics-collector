# Generated by Django 4.1.3 on 2022-11-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('lat', models.SmallIntegerField(verbose_name='широта')),
                ('lon', models.SmallIntegerField(verbose_name='долгота')),
                ('country', models.CharField(max_length=200, verbose_name='страна')),
            ],
        ),
    ]
