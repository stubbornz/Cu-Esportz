# Generated by Django 3.1.1 on 2020-09-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=7)),
            ],
        ),
    ]
