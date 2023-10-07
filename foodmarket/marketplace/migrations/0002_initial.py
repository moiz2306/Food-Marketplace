# Generated by Django 4.2.5 on 2023-10-05 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0001_initial'),
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='fooditem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.fooditem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]