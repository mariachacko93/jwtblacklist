# Generated by Django 3.1.5 on 2021-03-23 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeltest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('data', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
