# Generated by Django 2.1.2 on 2019-05-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('disk', models.IntegerField()),
                ('ip', models.CharField(max_length=15)),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'dev',
            },
        ),
    ]
