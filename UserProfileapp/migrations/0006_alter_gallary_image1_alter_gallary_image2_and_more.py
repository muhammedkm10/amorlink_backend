# Generated by Django 5.0.6 on 2024-05-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfileapp', '0005_patnerpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallary',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='user_gallary'),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='user_gallary'),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='user_gallary'),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='user_gallary'),
        ),
        migrations.AlterField(
            model_name='gallary',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='user_gallary'),
        ),
    ]
