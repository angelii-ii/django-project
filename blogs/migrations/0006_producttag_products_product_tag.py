# Generated by Django 4.2.7 on 2024-01-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_productinfo_products_product_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, verbose_name='تگ')),
            ],
            options={
                'verbose_name': ' تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='product_tag',
            field=models.ManyToManyField(to='blogs.producttag', verbose_name=' تگ محصول'),
        ),
    ]
