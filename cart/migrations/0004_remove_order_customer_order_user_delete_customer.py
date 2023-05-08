# Generated by Django 4.2 on 2023-05-07 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_favorite_pizza_alter_profile_image'),
        ('cart', '0003_remove_order_user_customer_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]