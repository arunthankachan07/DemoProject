# Generated by Django 3.2 on 2021-06-03 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20210603_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
