# Generated by Django 4.0.6 on 2022-07-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarytotal',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary_employee', to='manufacture.employee'),
        ),
    ]