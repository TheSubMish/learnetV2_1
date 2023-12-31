# Generated by Django 4.2.5 on 2023-09-19 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userlog.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(default='profilepic\\profile.jpg', upload_to=userlog.base.image_validation)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('edubackground', models.CharField(choices=[('1', 'Higher Secondary'), ('2', 'Diploma or Certificate Programs'), ('3', "Bachelor's Degree"), ('4', "Master's Degree"), ('5', 'Doctoral Degree (Ph.D.)')], default='1', max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.BooleanField(default=False, null=True)),
                ('css', models.BooleanField(default=False, null=True)),
                ('javascript', models.BooleanField(default=False, null=True)),
                ('python', models.BooleanField(default=False, null=True)),
                ('data_analysis', models.BooleanField(default=False, null=True)),
                ('data_structure_and_algorithms', models.BooleanField(default=False, null=True)),
                ('natural_language_processing', models.BooleanField(default=False, null=True)),
                ('machine_learning', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
