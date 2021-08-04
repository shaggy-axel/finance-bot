# Generated by Django 3.2.6 on 2021-08-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_income_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'names',
            },
        ),
        migrations.RemoveField(
            model_name='income',
            name='name',
        ),
        migrations.AddField(
            model_name='income',
            name='name',
            field=models.ManyToManyField(blank=True, to='finance_app.Name'),
        ),
    ]