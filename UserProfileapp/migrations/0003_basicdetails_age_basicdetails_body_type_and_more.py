# Generated by Django 5.0.6 on 2024-05-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfileapp', '0002_basicdetails_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='body_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='drinking_habits',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='eating_habits',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='hobbies',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='physical_status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='smalking_habits',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='basicdetails',
            name='weight',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
