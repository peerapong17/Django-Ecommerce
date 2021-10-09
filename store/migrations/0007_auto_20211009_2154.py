# Generated by Django 3.2.5 on 2021-10-09 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211006_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.orderstatus'),
        ),
    ]
