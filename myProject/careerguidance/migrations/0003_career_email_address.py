# Generated by Django 3.2.3 on 2021-06-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguidance', '0002_career_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='Email_address',
            field=models.EmailField(default=0, max_length=122),
            preserve_default=False,
        ),
    ]