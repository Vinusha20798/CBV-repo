# Generated by Django 3.1.3 on 2020-12-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.AlterField(
            model_name='hod',
            name='no',
            field=models.IntegerField(),
        ),
    ]
