# Generated by Django 4.2.7 on 2023-11-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0006_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('pic', models.ImageField(upload_to='Shepherds/%Y/%m/%d/')),
                ('type', models.CharField(blank=True, default='', max_length=125, null=True)),
            ],
        ),
    ]