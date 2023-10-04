# Generated by Django 4.2.5 on 2023-10-03 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_ssl_info_remove_skills_seeker_remove_summary_seeker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssl_info',
            name='seeker',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ssl_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
