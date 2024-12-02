# Generated by Django 5.1.3 on 2024-11-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('jop_time', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='clinic_and_sanatorium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotels/')),
                ('jop_time', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('tier', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Standard', 'Standard')], default='Standard', max_length=10)),
            ],
        ),
    ]
