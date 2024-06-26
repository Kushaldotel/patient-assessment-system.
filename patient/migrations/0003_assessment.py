# Generated by Django 5.0.6 on 2024-06-11 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(choices=[('cognitive', 'Cognitive Status'), ('physical', 'Physical Health'), ('mental', 'Mental Health'), ('emotional', 'Emotional Well-being'), ('social', 'Social Functioning'), ('nutrition', 'Nutritional Status'), ('functional', 'Functional Ability'), ('pain', 'Pain Assessment'), ('medication', 'Medication Adherence'), ('substance', 'Substance Use'), ('sleep', 'Sleep Quality'), ('environmental', 'Environmental Safety'), ('financial', 'Financial Stability')], max_length=20)),
                ('assessment_date', models.DateTimeField()),
                ('questions_and_answers', models.JSONField(default=list)),
                ('final_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='patient.patient')),
            ],
            options={
                'verbose_name': 'Assessment',
                'verbose_name_plural': 'Assessments',
            },
        ),
    ]
