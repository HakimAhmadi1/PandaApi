# Generated by Django 4.2.5 on 2023-09-23 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employer', '0005_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='employer.jobs'),
        ),
        migrations.AlterField(
            model_name='application',
            name='seeker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
    ]
