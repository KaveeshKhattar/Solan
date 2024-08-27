# Generated by Django 2.1.3 on 2019-02-27 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciscoapp', '0010_auto_20190129_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chp', models.CharField(db_column='chp', max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subchap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ciscoapp.chapter')),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='chp',
        ),
        migrations.AddField(
            model_name='subchap',
            name='sub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ciscoapp.subject'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciscoapp.subject'),
        ),
    ]
