# Generated by Django 5.0.6 on 2024-06-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
