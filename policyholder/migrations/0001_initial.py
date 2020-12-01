# Generated by Django 3.0.3 on 2020-11-23 12:02

import datetime
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfallback.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contribution_plan', '0002_auto_20201120_1143'),
        ('insuree', '0004_confirmationtype_education_profession_relation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0005_healthfacilitycatchment_healthfacilitylegalform_healthfacilitymutation_healthfacilitysublevel'),
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyHolder',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(blank=True, db_column='PolicyHolderCode', max_length=32, null=True)),
                ('trade_name', models.CharField(db_column='TradeName', max_length=255)),
                ('address', models.CharField(db_column='Address', max_length=255)),
                ('phone', models.CharField(db_column='Phone', max_length=16)),
                ('fax', models.CharField(db_column='Fax', max_length=16)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('contact_name', models.CharField(db_column='ContractName', max_length=255)),
                ('legal_form', models.IntegerField(db_column='LegalForm')),
                ('activity_code', models.IntegerField(db_column='ActivityCode')),
                ('accountancy_account', models.CharField(db_column='AccountancyAccount', max_length=255)),
                ('payment_reference', models.CharField(db_column='PaymentReference', max_length=255)),
                ('locations_uuid', models.ManyToManyField(blank=True, to='location.Location', verbose_name='LocationsUUID')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholder_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholder_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblPolicyHolder',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PolicyHolderUser',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('policy_holder', models.ForeignKey(db_column='PolicyHolderId', on_delete=django.db.models.deletion.DO_NOTHING, to='policyholder.PolicyHolder')),
                ('user', models.ForeignKey(db_column='UserUUID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholderuser_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholderuser_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblPolicyHolderUser',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PolicyHolderInsuree',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('contribution_plan_bundle', models.ForeignKey(db_column='ContribuiotnPlanBundleId', on_delete=django.db.models.deletion.DO_NOTHING, to='contribution_plan.ContributionPlanBundle')),
                ('insuree', models.ForeignKey(db_column='InsureeId', on_delete=django.db.models.deletion.DO_NOTHING, to='insuree.Insuree')),
                ('last_policy', models.ForeignKey(db_column='LastPolicyId', on_delete=django.db.models.deletion.DO_NOTHING, to='policy.Policy')),
                ('policy_holder', models.ForeignKey(db_column='PolicyHolderId', on_delete=django.db.models.deletion.DO_NOTHING, to='policyholder.PolicyHolder')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholderinsuree_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholderinsuree_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblPolicyHolderInsuree',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PolicyHolderContributionPlan',
            fields=[
                ('id', models.UUIDField(db_column='UUID', default=None, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('contribution_plan_bundle', models.ForeignKey(db_column='ContribuiotnPlanBundleId', on_delete=django.db.models.deletion.DO_NOTHING, to='contribution_plan.ContributionPlanBundle')),
                ('policy_holder', models.ForeignKey(db_column='PolicyHolderId', on_delete=django.db.models.deletion.DO_NOTHING, to='policyholder.PolicyHolder')),
                ('user_created', models.ForeignKey(db_column='UserCreatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholdercontributionplan_user_created', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(db_column='UserUpdatedUUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='policyholdercontributionplan_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblPolicyHolderContributionPlan',
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPolicyHolderUser',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('policy_holder', models.ForeignKey(blank=True, db_column='PolicyHolderId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='policyholder.PolicyHolder')),
                ('user', models.ForeignKey(blank=True, db_column='UserUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical policy holder user',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPolicyHolderInsuree',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('contribution_plan_bundle', models.ForeignKey(blank=True, db_column='ContribuiotnPlanBundleId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contribution_plan.ContributionPlanBundle')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('insuree', models.ForeignKey(blank=True, db_column='InsureeId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='insuree.Insuree')),
                ('last_policy', models.ForeignKey(blank=True, db_column='LastPolicyId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='policy.Policy')),
                ('policy_holder', models.ForeignKey(blank=True, db_column='PolicyHolderId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='policyholder.PolicyHolder')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical policy holder insuree',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPolicyHolderContributionPlan',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('contribution_plan_bundle', models.ForeignKey(blank=True, db_column='ContribuiotnPlanBundleId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contribution_plan.ContributionPlanBundle')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('policy_holder', models.ForeignKey(blank=True, db_column='PolicyHolderId', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='policyholder.PolicyHolder')),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical policy holder contribution plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPolicyHolder',
            fields=[
                ('id', models.UUIDField(db_column='UUID', db_index=True, default=None, editable=False)),
                ('is_deleted', models.BooleanField(db_column='isDeleted', default=False)),
                ('json_ext', jsonfallback.fields.FallbackJSONField(blank=True, db_column='Json_ext', null=True)),
                ('date_created', models.DateTimeField(db_column='DateCreated', null=True)),
                ('date_updated', models.DateTimeField(db_column='DateUpdated', null=True)),
                ('version', models.IntegerField(default=1)),
                ('date_valid_from', models.DateTimeField(db_column='DateValidFrom', default=datetime.datetime.now)),
                ('date_valid_to', models.DateTimeField(blank=True, db_column='DateValidTo', null=True)),
                ('replacement_uuid', models.UUIDField(db_column='ReplacementUUID', null=True)),
                ('code', models.CharField(blank=True, db_column='PolicyHolderCode', max_length=32, null=True)),
                ('trade_name', models.CharField(db_column='TradeName', max_length=255)),
                ('address', models.CharField(db_column='Address', max_length=255)),
                ('phone', models.CharField(db_column='Phone', max_length=16)),
                ('fax', models.CharField(db_column='Fax', max_length=16)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('contact_name', models.CharField(db_column='ContractName', max_length=255)),
                ('legal_form', models.IntegerField(db_column='LegalForm')),
                ('activity_code', models.IntegerField(db_column='ActivityCode')),
                ('accountancy_account', models.CharField(db_column='AccountancyAccount', max_length=255)),
                ('payment_reference', models.CharField(db_column='PaymentReference', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(blank=True, db_column='UserCreatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, db_column='UserUpdatedUUID', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical policy holder',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
