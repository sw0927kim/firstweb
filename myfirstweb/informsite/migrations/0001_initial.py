# Generated by Django 5.0.6 on 2024-05-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposer', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
