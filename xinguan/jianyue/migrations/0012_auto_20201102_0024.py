# Generated by Django 3.1.1 on 2020-11-02 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jianyue', '0011_auto_20201101_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jishiqitadizhi',
            old_name='shenqingqingkuang',
            new_name='zhuangtai',
        ),
        migrations.DeleteModel(
            name='renyuananpai',
        ),
    ]
