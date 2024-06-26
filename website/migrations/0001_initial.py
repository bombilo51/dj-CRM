# Generated by Django 5.0.3 on 2024-03-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('iin', models.CharField(max_length=12)),
                ('udo_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
