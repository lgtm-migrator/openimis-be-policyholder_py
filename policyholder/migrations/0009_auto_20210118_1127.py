# Generated by Django 3.0.3 on 2021-01-18 11:27

import core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policyholder', '0008_auto_20210118_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpolicyholder',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholder',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholder',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholder',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholdercontributionplan',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholdercontributionplan',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholdercontributionplan',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholdercontributionplan',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderinsuree',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderinsuree',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderinsuree',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderinsuree',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderuser',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderuser',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderuser',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='historicalpolicyholderuser',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='policyholdercontributionplan',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholdercontributionplan',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholdercontributionplan',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='policyholdercontributionplan',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderinsuree',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderinsuree',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderinsuree',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='policyholderinsuree',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderuser',
            name='date_created',
            field=core.fields.DateTimeField(db_column='DateCreated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderuser',
            name='date_updated',
            field=core.fields.DateTimeField(db_column='DateUpdated', null=True),
        ),
        migrations.AlterField(
            model_name='policyholderuser',
            name='date_valid_from',
            field=core.fields.DateTimeField(db_column='DateValidFrom'),
        ),
        migrations.AlterField(
            model_name='policyholderuser',
            name='date_valid_to',
            field=core.fields.DateTimeField(blank=True, db_column='DateValidTo', null=True),
        ),
    ]
