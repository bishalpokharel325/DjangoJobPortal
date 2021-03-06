# Generated by Django 3.1.2 on 2020-10-20 14:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=150)),
                ('created_at', models.DateField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('no', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
