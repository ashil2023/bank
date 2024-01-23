# Generated by Django 4.2.6 on 2024-01-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('district', models.CharField(max_length=255)),
                ('Account', models.CharField(max_length=255)),
                ('Account1', models.CharField(max_length=255)),
                ('Debit', models.CharField(max_length=255)),
                ('Credit', models.CharField(max_length=255)),
                ('Cheque', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]