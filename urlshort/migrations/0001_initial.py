# Generated by Django 3.1.3 on 2020-11-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('shorturl', models.CharField(max_length=8)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
