# Generated by Django 4.0.4 on 2022-05-11 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_payment_card_number_payment_cvv_payment_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name_on_card',
            field=models.CharField(max_length=100),
        ),
    ]
