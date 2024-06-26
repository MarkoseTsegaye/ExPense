# Generated by Django 5.0.6 on 2024-06-24 02:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('name', models.CharField(max_length=9999, null=True)),
                ('category', models.CharField(choices=[('Housing', 'HOUSING'), ('Food', 'FOOD'), ('Clothing', 'CLOTHING'), ('Auto', 'AUTO'), ('Insurance', 'INSURANCE'), ('Gym', 'GYM'), ('Loan', 'LOAN')], default='Food', max_length=999)),
                ('date', models.DateField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Warning', models.BooleanField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('Housing', 'HOUSING'), ('Food', 'FOOD'), ('Clothing', 'CLOTHING'), ('Auto', 'AUTO'), ('Insurance', 'INSURANCE'), ('Gym', 'GYM'), ('Loan', 'LOAN')], default='Food', max_length=999)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('source', models.CharField(max_length=9999)),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('setup', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
