# Generated by Django 5.1.3 on 2024-11-27 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_notification_test'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalrecord',
            old_name='recommended_treatment',
            new_name='treatments',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='weight',
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medical_record', to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('appointment', 'Appointment'), ('test', 'Test'), ('medication', 'Medication')], max_length=20),
        ),
        migrations.AlterField(
            model_name='notification',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]