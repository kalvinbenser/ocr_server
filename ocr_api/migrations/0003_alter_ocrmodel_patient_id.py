# Generated by Django 4.2.2 on 2023-06-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_api', '0002_alter_ocrmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocrmodel',
            name='patient_id',
            field=models.IntegerField(unique=True),
        ),
    ]
