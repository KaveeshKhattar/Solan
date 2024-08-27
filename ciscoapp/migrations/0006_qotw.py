# Generated by Django 2.1.3 on 2019-01-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciscoapp', '0005_auto_20190104_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='qotw',
            fields=[
                ('subject', models.CharField(db_column='subject', max_length=80, primary_key=True, serialize=False)),
                ('chapter', models.CharField(db_column='chapter', max_length=80)),
                ('question', models.CharField(db_column='question', max_length=1000)),
                ('option1', models.CharField(db_column='option1', max_length=500)),
                ('option2', models.CharField(db_column='option2', max_length=500)),
                ('option3', models.CharField(db_column='option3', max_length=500)),
                ('option4', models.CharField(db_column='option4', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'qotw',
                'db_table': 'qotw',
            },
        ),
    ]
