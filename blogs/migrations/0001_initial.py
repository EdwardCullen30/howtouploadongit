# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-26 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=30, null=True)),
                ('blogger_name', models.CharField(default=None, max_length=30, null=True)),
                ('blogger_desc', models.TextField()),
                ('blogger_email', models.CharField(max_length=40, null=True)),
                ('image', models.ImageField(null=True, upload_to='profile_image')),
                ('insta', models.URLField(blank=True, max_length=100, null=True)),
                ('fb', models.URLField(blank=True, max_length=100, null=True)),
                ('twitter', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, null=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_detail', models.TextField()),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Blogger')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.Post'),
        ),
    ]
