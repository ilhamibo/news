# Generated by Django 2.2.2 on 2019-06-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
    ]