# Generated by Django 5.0.2 on 2024-03-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0019_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='clouds',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='Clouds/%Y/%m/%d/'),
        ),
    ]
