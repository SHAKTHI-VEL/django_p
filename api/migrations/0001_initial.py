# Generated by Django 5.0 on 2023-12-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=200)),
                ('leadname', models.CharField(max_length=200)),
                ('prn', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('mem1', models.CharField(max_length=200)),
                ('prn1', models.CharField(max_length=200)),
                ('email1', models.CharField(max_length=200)),
                ('contact1', models.CharField(max_length=200)),
                ('mem2', models.CharField(max_length=200)),
                ('prn2', models.CharField(max_length=200)),
                ('email2', models.CharField(max_length=200)),
                ('contact2', models.CharField(max_length=200)),
                ('mem3', models.CharField(max_length=200)),
                ('prn3', models.CharField(max_length=200)),
                ('email3', models.CharField(max_length=200)),
                ('contact3', models.CharField(max_length=200)),
            ],
        ),
    ]
