# Generated by Django 3.1.1 on 2020-11-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianyue', '0016_auto_20201105_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='faxing',
            name='faxingming',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
