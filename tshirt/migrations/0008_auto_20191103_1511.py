# Generated by Django 2.2.6 on 2019-11-03 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tshirt', '0007_auto_20191103_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='tshirt.Tshirt'),
        ),
    ]