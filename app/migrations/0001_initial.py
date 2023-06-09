# Generated by Django 4.1.7 on 2023-04-07 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('DEPTNO', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=100)),
                ('LOC', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='emplyee',
            fields=[
                ('EMPNO', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=100)),
                ('JOB', models.CharField(max_length=100)),
                ('MGR', models.IntegerField()),
                ('HIREDATE', models.DateField()),
                ('SAL', models.IntegerField()),
                ('COMM', models.IntegerField()),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]
