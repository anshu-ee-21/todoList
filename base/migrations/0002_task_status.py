# Generated by Django 3.0 on 2023-05-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Under Progress', 'Under Progress'), ('Complete', 'Complete')], max_length=200, null=True),
        ),
    ]
