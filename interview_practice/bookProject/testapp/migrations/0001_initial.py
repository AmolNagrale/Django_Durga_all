# Generated by Django 3.2.7 on 2022-01-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('salary', models.IntegerField()),
                ('qualification', models.CharField(max_length=64)),
            ],
        ),
    ]
