# Generated by Django 4.2 on 2023-05-10 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_contactinformation_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinformation',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='zipcode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
