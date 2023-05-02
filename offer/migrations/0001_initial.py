# Generated by Django 4.2 on 2023-05-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('member_since', models.DateTimeField()),
                ('image', models.CharField(blank=True, max_length=9999)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('favorite_pizza', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pizza.menupizzas')),
            ],
        ),
    ]
