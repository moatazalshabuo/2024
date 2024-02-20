# Generated by Django 4.1 on 2024-02-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0010_alter_booking_suite_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('project_title', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('status', models.IntegerField(blank=True, default=1, null=True)),
                ('detiles', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
