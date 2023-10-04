# Generated by Django 4.2.5 on 2023-09-20 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.TextField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('hiring_number', models.CharField(blank=True, max_length=100, null=True)),
                ('hiring_country', models.CharField(blank=True, max_length=50, null=True)),
                ('hiring_city', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('phase', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('salary_rate', models.CharField(blank=True, max_length=50, null=True)),
                ('salary_start_range', models.IntegerField(blank=True, null=True)),
                ('salary_end_range', models.IntegerField(blank=True, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('shortlisted_candidate', models.CharField(blank=True, max_length=50, null=True)),
                ('interview_candidate', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.CharField(blank=True, max_length=50, null=True)),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employer.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Job_PreScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=150, null=True)),
                ('required', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(blank=True, choices=[('Required', 'Required'), ('Not Required', 'Not Required'), ('Optional', 'Optional')], max_length=50, null=True)),
                ('send_update_to', models.CharField(blank=True, max_length=150, null=True)),
                ('application_deadline', models.DateField(blank=True, null=True)),
                ('hiring_timeline', models.CharField(blank=True, max_length=50, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('ntn', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_number', models.CharField(blank=True, max_length=100, null=True)),
                ('operating_since', models.IntegerField(blank=True, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]