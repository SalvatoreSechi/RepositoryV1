# Generated by Django 2.2.19 on 2021-03-25 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
                ('giornalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Giornalista')),
            ],
        ),
    ]
