# Generated by Django 4.2.7 on 2023-11-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0002_besicdata_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besicdata',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
