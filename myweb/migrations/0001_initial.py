# Generated by Django 4.0.4 on 2022-06-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('namet', models.TextField(null=True)),
                ('stat', models.CharField(default=1, max_length=2)),
                ('tiam', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
