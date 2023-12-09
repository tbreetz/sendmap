# Generated by Django 4.2.6 on 2023-11-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_tick_unique_ticks_tick_unique_ticks'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tick',
            name='unique ticks',
        ),
        migrations.AddConstraint(
            model_name='tick',
            constraint=models.UniqueConstraint(fields=('user', 'date', 'name', 'crag'), name='unique ticks'),
        ),
    ]
