# Generated by Django 3.0.7 on 2020-06-26 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast_or_roast', models.CharField(choices=[('B', 'Boast'), ('R', 'Roast')], max_length=1)),
                ('content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
