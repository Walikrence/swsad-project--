# Generated by Django 2.1.7 on 2019-06-25 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0008_auto_20190625_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option_vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(default='null', max_length=128)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paper.Option')),
            ],
        ),
        migrations.AddField(
            model_name='question_fill_answer',
            name='author',
            field=models.CharField(default='null', max_length=128),
        ),
        migrations.AlterField(
            model_name='question_fill_answer',
            name='answer',
            field=models.CharField(max_length=128),
        ),
    ]
