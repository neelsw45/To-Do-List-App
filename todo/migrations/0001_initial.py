# Generated by Django 5.1.3 on 2024-12-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=100)),
                ('tdesc', models.CharField(max_length=5000)),
            ],
        ),
    ]
