# Generated by Django 4.0.1 on 2022-01-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usercomplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=200)),
                ('di', models.IntegerField(unique=True)),
                ('sub', models.CharField(max_length=250)),
                ('comp', models.TextField()),
                ('addedon', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Complaint Table',
            },
        ),
    ]
