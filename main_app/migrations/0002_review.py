# Generated by Django 4.1.1 on 2022-10-26 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('review', models.TextField(max_length=250)),
                ('Magnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.magnet')),
            ],
        ),
    ]
