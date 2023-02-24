# Generated by Django 3.2 on 2022-12-30 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_auto_20221229_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depts', to='a1.college'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='college',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='princi', to='a1.college'),
        ),
        migrations.AlterField(
            model_name='student1',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studs', to='a1.department'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subj', to='a1.department'),
        ),
    ]
