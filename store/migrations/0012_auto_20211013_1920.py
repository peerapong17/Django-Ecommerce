# Generated by Django 3.2.5 on 2021-10-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_orderstatus_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.ManyToManyField(null=True, to='store.Promotion'),
        ),
    ]
