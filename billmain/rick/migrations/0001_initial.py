# Generated by Django 2.2.19 on 2022-09-02 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_profile', models.CharField(max_length=200)),
                ('rick_name', models.CharField(max_length=70)),
                ('rick_image', models.CharField(max_length=70)),
                ('rick_species', models.CharField(max_length=70)),
                ('rick_status', models.CharField(max_length=70)),
                ('rick_location', models.CharField(max_length=70)),
                ('rick_first_episode', models.CharField(max_length=70)),
            ],
        ),
    ]
