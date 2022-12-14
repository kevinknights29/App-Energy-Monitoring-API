# Generated by Django 4.1.1 on 2022-11-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_room_alter_measurement_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.room'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.room'),
        ),
    ]
