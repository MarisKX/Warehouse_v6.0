# Generated by Django 4.2.1 on 2023-06-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings_number', models.CharField(default='0000xxxx', max_length=8)),
                ('valid_from', models.DateField()),
                ('valid_till', models.DateField()),
                ('acions_per_day', models.PositiveIntegerField(default=1)),
                ('vsaoi_dn', models.DecimalField(decimal_places=2, max_digits=4)),
                ('iin_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('no_iin_level', models.DecimalField(decimal_places=2, max_digits=8)),
                ('uin_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('enviroment_tax_base', models.DecimalField(decimal_places=2, max_digits=8)),
                ('btw', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vsaoi_dd', models.DecimalField(decimal_places=2, max_digits=4)),
                ('base_cadastre_value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('valid', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Basic Settings',
            },
        ),
    ]
