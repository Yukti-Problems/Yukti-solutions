# Generated by Django 4.0.6 on 2022-08-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=50)),
                ('cname', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('nba_aggregated', models.CharField(max_length=5)),
                ('duration_of_nba_aggregration', models.CharField(max_length=20, null=True)),
                ('Student_Faculty_Ratio', models.FloatField()),
            ],
        ),
    ]
