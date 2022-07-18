# Generated by Django 4.0.5 on 2022-07-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_of_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_post',
            field=models.ManyToManyField(related_name='likers', to='network.post'),
        ),
    ]
