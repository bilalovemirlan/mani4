# Generated by Django 4.0.6 on 2022-07-21 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacture', '0006_rename_client_name_client_name_client_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='defect_machine',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='defect_saya',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='file',
            field=models.FileField(blank=True, upload_to='media/clients/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='production',
            name='defect_worker',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='DailyTimesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacture.employee')),
            ],
        ),
        migrations.CreateModel(
            name='DailyProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('defect_worker', models.PositiveIntegerField(default=0)),
                ('defect_machine', models.PositiveIntegerField(default=0)),
                ('defect_saya', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_pro_catalogue', to='manufacture.catalogue')),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacture.dailytimesheet')),
            ],
        ),
    ]
