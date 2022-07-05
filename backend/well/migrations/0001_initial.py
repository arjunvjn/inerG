# Generated by Django 2.2.5 on 2022-07-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ohio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_well_number', models.CharField(max_length=15)),
                ('quater', models.CharField(max_length=2)),
                ('oil', models.FloatField(default=0)),
                ('gas', models.FloatField(default=0)),
                ('brine', models.FloatField(default=0)),
            ],
        ),
    ]