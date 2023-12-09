# Generated by Django 4.2.6 on 2023-11-16 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='tick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('route_type', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('grade', models.CharField(max_length=10)),
                ('crag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.crag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]
