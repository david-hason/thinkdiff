# Generated by Django 2.0.5 on 2018-05-20 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.QuoteCategory'),
        ),
    ]
