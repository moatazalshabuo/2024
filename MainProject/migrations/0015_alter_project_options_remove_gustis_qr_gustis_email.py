# Generated by Django 4.1 on 2024-02-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainProject', '0014_project_universty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='gustis',
            name='qr',
        ),
        migrations.AddField(
            model_name='gustis',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]