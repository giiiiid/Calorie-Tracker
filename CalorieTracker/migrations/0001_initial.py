# Generated by Django 4.2.2 on 2023-09-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.FloatField()),
            ],
        ),
    ]