# Generated by Django 3.0.5 on 2020-04-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlgym1', '0003_auto_20200422_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThetaString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('theta_string', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
