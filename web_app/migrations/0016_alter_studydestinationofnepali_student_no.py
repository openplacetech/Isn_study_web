# Generated by Django 4.0 on 2024-07-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0015_applyforcurrier_availability_or_notice_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studydestinationofnepali',
            name='student_no',
            field=models.CharField(max_length=100),
        ),
    ]
