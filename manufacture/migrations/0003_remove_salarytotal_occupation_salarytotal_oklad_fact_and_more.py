# Generated by Django 4.0.6 on 2022-07-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0002_salarytotal_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salarytotal',
            name='occupation',
        ),
        migrations.AddField(
            model_name='salarytotal',
            name='oklad_fact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salarytotal',
            name='oklad_social_fund',
            field=models.IntegerField(null=True),
        ),
    ]