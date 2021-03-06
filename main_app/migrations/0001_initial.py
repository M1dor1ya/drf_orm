# Generated by Django 2.1.2 on 2019-05-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('graph_name', models.CharField(max_length=255)),
                ('graph_content', models.TextField()),
                ('graph_status', models.BooleanField(default=False)),
                ('graph_conf', models.CharField(max_length=255)),
                ('graph_position', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'graph',
            },
        ),
    ]
