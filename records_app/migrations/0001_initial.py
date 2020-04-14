# Generated by Django 3.0.4 on 2020-03-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('date', models.DateTimeField()),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField()),
                ('pulse', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'record',
            },
        ),
        migrations.AddIndex(
            model_name='record',
            index=models.Index(fields=['user_id'], name='record_user_id_a84bd3_idx'),
        ),
        migrations.AddIndex(
            model_name='record',
            index=models.Index(fields=['date'], name='record_date_b7a05c_idx'),
        ),
    ]
