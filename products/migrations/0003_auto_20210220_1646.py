# Generated by Django 3.1.7 on 2021-02-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210220_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo9',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]