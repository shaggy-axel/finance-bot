# Generated by Django 3.2.6 on 2021-08-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0003_auto_20210804_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'asset_names',
            },
        ),
        migrations.CreateModel(
            name='NameExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'expense_names',
            },
        ),
        migrations.RenameModel(
            old_name='Name',
            new_name='NameIncome',
        ),
        migrations.AlterModelTable(
            name='nameincome',
            table='income_names',
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(choices=[('RUR', 'RUR'), ('USD', 'USD'), ('EUR', 'EUR'), ('CZK', 'CZK')], default='RUR', max_length=255)),
                ('date_expense', models.DateTimeField(auto_now_add=True)),
                ('name', models.ManyToManyField(blank=True, to='finance_app.NameExpense')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(choices=[('RUR', 'RUR'), ('USD', 'USD'), ('EUR', 'EUR'), ('CZK', 'CZK')], default='RUR', max_length=255)),
                ('date_purchase', models.DateTimeField(auto_now_add=True)),
                ('name', models.ManyToManyField(blank=True, to='finance_app.NameAsset')),
            ],
        ),
    ]
