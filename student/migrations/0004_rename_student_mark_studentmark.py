# Generated by Django 4.2.5 on 2023-10-04 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_coursetitle'),
        ('student', '0003_student_mark_enroll'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_Mark',
            new_name='StudentMark',
        ),
    ]
