# Generated by Django 5.1.4 on 2025-01-13 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre_alter_book_state_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='books.country'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('Ha', 'Hardcover'), ('So', 'Softcover')], default='So', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='state',
            field=models.CharField(choices=[('Gd', 'Used Good'), ('Ne', 'New'), ('Po', 'Used Poor'), ('Fr', 'Used Fair'), ('Ex', 'Used Excellent')], default='Ex', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]