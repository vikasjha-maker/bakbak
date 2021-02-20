# Generated by Django 3.1.6 on 2021-02-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210218_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='accounts/images')),
            ],
        ),
    ]
