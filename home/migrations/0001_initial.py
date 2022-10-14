# Generated by Django 3.1.2 on 2022-10-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('imageUrl', models.CharField(max_length=2000)),
            ],
        ),
    ]