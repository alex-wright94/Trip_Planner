# Generated by Django 2.2.4 on 2019-08-26 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination', models.CharField(max_length=255)),
                ('Travel_start_date', models.DateTimeField()),
                ('Desc', models.TextField(max_length=255)),
                ('Travel_end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_added', to='newapp.User')),
                ('users', models.ManyToManyField(related_name='trips', to='newapp.User')),
            ],
        ),
    ]
