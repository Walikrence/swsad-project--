# Generated by Django 2.1.7 on 2019-06-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190625_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456', max_length=256),
        ),
    ]
