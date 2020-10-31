# Generated by Django 3.1.2 on 2020-10-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('human_name', models.CharField(max_length=100)),
                ('human_dob', models.DateField()),
                ('human_gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20)),
            ],
        ),
    ]
