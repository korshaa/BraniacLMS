# Generated by Django 3.2 on 2022-09-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_data_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('course', 'num')},
        ),
        migrations.AddField(
            model_name='news',
            name='test',
            field=models.CharField(blank=True, max_length=256, verbose_name='Title'),
        ),
    ]
