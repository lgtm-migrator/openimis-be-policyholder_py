# Generated by Django 3.0.3 on 2020-11-26 10:19

from django.db import migrations
import jsonfallback.fields


class Migration(migrations.Migration):

    dependencies = [
        ('policyholder', '0007_auto_20201126_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpolicyholder',
            name='address',
            field=jsonfallback.fields.FallbackJSONField(blank=True, db_column='Address', null=True),
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='address',
            field=jsonfallback.fields.FallbackJSONField(blank=True, db_column='Address', null=True),
        ),
    ]
