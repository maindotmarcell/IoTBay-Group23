# Generated by Django 4.0.4 on 2022-05-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='card_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='cvv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='expiry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='name_on_card',
            field=models.CharField(max_length=50, null=True),
        ),
    ]