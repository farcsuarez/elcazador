# Generated by Django 5.1.4 on 2025-01-13 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.country')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.country')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('pub_year', models.PositiveSmallIntegerField()),
                ('cover', models.CharField(choices=[('So', 'Softcover'), ('Ha', 'Hardcover')], default='So', max_length=2)),
                ('state', models.CharField(choices=[('Fr', 'Used Fair'), ('Gd', 'Used Good'), ('Ne', 'New'), ('Po', 'Used Poor'), ('Ex', 'Used Excellent')], default='Ex', max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('pages', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('authors', models.ManyToManyField(to='books.author')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.editor')),
            ],
        ),
    ]