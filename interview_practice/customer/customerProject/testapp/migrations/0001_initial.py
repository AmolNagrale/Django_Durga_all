# Generated by Django 3.2.7 on 2022-01-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('eno', models.IntegerField()),
                ('mailid', models.CharField(max_length=64)),
                ('phonenumber', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
