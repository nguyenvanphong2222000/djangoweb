# Generated by Django 4.1.2 on 2022-11-01 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_entry_active_entry_updated_date_alter_entry_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='active',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='updated_date',
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
    ]
