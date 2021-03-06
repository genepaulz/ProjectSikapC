# Generated by Django 3.2.4 on 2021-06-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('yearsOfExperience', models.IntegerField()),
                ('position', models.CharField(max_length=100)),
                ('dateAdded', models.DateTimeField()),
                ('isAgeViewable', models.IntegerField()),
                ('isDeleted', models.IntegerField()),
                ('applicantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.applicant')),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
    ]
