# Generated by Django 3.2.4 on 2021-06-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_applicant_ratings'),
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='raterEmail',
            field=models.ManyToManyField(blank=True, null=True, to='login.Employer'),
        ),
    ]
