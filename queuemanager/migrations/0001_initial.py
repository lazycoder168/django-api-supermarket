# Generated by Django 3.2.7 on 2021-09-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_queue', models.CharField(max_length=10)),
                ('choice_estimated', models.CharField(max_length=30)),
            ],
        ),
    ]
