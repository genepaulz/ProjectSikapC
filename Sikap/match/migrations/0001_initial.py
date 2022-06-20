# Generated by Django 3.2.4 on 2022-06-16 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_alter_posts_applicantid'),
        ('login', '0003_remove_user_companyname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicantID', models.ForeignKey(db_column='applicantID', on_delete=django.db.models.deletion.CASCADE, to='login.applicant')),
                ('employerID', models.ForeignKey(db_column='employerID', on_delete=django.db.models.deletion.CASCADE, to='login.employer')),
                ('postsID', models.ForeignKey(db_column='postsID', on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
            options={
                'db_table': 'Match',
            },
        ),
    ]
