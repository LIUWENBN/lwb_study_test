# Generated by Django 4.2.4 on 2023-09-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
