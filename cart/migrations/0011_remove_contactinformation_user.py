# Generated by Django 4.2 on 2023-05-10 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_contactinformation_address_contactinformation_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation',
            name='user',
        ),
    ]
