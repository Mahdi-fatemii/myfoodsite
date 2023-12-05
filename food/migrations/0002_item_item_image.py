# Generated by Django 4.2.7 on 2023-12-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/png;base64,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', max_length=1000),
        ),
    ]
