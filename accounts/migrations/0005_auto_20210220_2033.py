# Generated by Django 3.1.6 on 2021-02-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210220_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insta',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]