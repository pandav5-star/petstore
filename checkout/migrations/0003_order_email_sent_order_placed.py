# Generated by Django 5.1 on 2024-10-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_oreder_item_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='placed',
            field=models.BooleanField(default=False),
        ),
    ]
