# Generated by Django 5.1.4 on 2024-12-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='school_fees',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]