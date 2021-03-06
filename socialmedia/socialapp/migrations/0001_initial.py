# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CateUsr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=True)),
                ('categ', models.ForeignKey(to='socialapp.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_body', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('R_check', models.IntegerField(default=0)),
                ('c_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(default=b'1.jpeg', upload_to=b'upload', blank=True)),
                ('p_body', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cat_name', models.ForeignKey(to='socialapp.Category')),
                ('dislike', models.ManyToManyField(related_name='dislike', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('like', models.ManyToManyField(related_name='like', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('R_body', models.CharField(max_length=255)),
                ('time_reply', models.DateTimeField()),
                ('R_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(to='socialapp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Unwanted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='id_post',
            field=models.ForeignKey(to='socialapp.Posts'),
        ),
    ]
