# Generated by Django 3.2 on 2022-12-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('adr', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('dept_str', models.IntegerField(null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depts', to='a1.college')),
            ],
            options={
                'db_table': 'department',
                'unique_together': {('name', 'college')},
            },
        ),
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('marks', models.IntegerField(null=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studs', to='a1.department')),
            ],
            options={
                'db_table': 'student1',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('is_practical', models.BooleanField(null=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjs', to='a1.department')),
                ('student', models.ManyToManyField(to='a1.Student1')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('qual', models.CharField(max_length=10, null=True)),
                ('exp', models.IntegerField(null=True)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='princi', to='a1.college')),
            ],
            options={
                'db_table': 'principal',
            },
        ),
    ]
