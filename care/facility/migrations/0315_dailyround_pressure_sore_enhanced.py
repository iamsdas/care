# Generated by Django 2.2.11 on 2022-09-05 08:02

import care.utils.models.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0314_patientconsultation_icd11_diagnoses'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyround',
            name='pressure_sore_enhanced',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list, validators=[care.utils.models.validators.JSONFieldSchemaValidator({'$schema': 'http://json-schema.org/draft-07/schema#', 'items': [{'additionalProperties': False, 'properties': {'description': {'type': 'string'}, 'exudate_amount': {'enum': ['None', 'Light', 'Moderate', 'Heavy']}, 'length': {'type': 'number'}, 'push_score': {'type': 'number'}, 'tissue_type': {'enum': ['Closed', 'Epithelial', 'Granulation', 'Slough', 'Necrotic']}, 'width': {'type': 'number'}}, 'required': ['length', 'width', 'exudate_amount', 'tissue_type', 'description'], 'type': 'object'}], 'type': 'array'})]),
        ),
    ]
