# Generated by Django 3.0.6 on 2020-06-20 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0031_auto_20200609_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved',
            field=models.ManyToManyField(to='syllabiShare.Submission'),
        ),
    ]
