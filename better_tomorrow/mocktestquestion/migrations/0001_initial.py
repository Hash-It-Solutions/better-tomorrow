# Generated by Django 3.1 on 2022-12-26 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('mocktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MockTestQuestion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField(max_length=500)),
                ('mock_test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mocktest.mocktest')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.subject')),
            ],
        ),
    ]
