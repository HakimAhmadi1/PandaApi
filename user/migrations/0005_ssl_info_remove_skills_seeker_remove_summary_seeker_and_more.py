# Generated by Django 4.2.5 on 2023-10-03 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_alter_seeker_info_seeker'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSL_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('skill', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='skills',
            name='seeker',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='seeker',
        ),
        migrations.DeleteModel(
            name='Languages',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
    ]