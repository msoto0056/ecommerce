# Generated by Django 3.1.7 on 2021-03-01 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210301_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
