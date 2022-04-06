# Generated by Django 4.0.1 on 2022-04-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.CharField(max_length=20)),
                ('bname', models.CharField(max_length=20)),
                ('aname', models.CharField(max_length=20)),
                ('categ', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
