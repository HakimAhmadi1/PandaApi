# Generated by Django 4.2.5 on 2023-09-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Shortlist', 'Shortlist'), ('Interview', 'Interview'), ('Reject', 'Reject')], default='Pending', max_length=50, null=True),
        ),
    ]