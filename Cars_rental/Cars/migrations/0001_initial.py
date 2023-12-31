# Generated by Django 4.2.4 on 2023-10-15 17:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('c_price', models.IntegerField()),
                ('c_slug', models.SlugField(blank=True, null=True, unique_for_date='c_publish')),
                ('c_model', models.IntegerField()),
                ('c_type', models.CharField(max_length=30)),
                ('c_status', models.BooleanField(default=True)),
                ('c_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('c_details', models.TextField(null=True)),
                ('c_publish', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=30)),
                ('b_phone', models.BigIntegerField()),
                ('b_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('b_exdate', models.DateField()),
                ('b_status', models.BooleanField(default=True)),
                ('b_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_bookings', to='Cars.car')),
            ],
        ),
    ]
