# Generated by Django 5.1.6 on 2025-03-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KisilikTesti', '0003_kisilik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kisilik',
            name='id',
        ),
        migrations.AlterField(
            model_name='kisilik',
            name='kategori',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
