# Generated by Django 3.0.6 on 2020-06-02 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabiShare', '0016_auto_20200601_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='school_fk_temp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabiShare.School'),
        ),
    ]