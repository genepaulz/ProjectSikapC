# Generated by Django 3.2.4 on 2021-06-13 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_applicant_ratings'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='applicantID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.applicant'),
        ),
    ]