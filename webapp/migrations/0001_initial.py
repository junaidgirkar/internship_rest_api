# Generated by Django 3.1.5 on 2021-01-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('Sno', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('job_id', models.IntegerField()),
                ('position', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('package', models.BigIntegerField()),
                ('skills_required', models.CharField(max_length=255)),
                ('experience_required', models.IntegerField()),
            ],
        ),
    ]