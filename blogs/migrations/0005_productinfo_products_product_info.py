# Generated by Django 4.2.7 on 2024-01-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_productcategory_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=150, verbose_name='رنگ')),
                ('size', models.CharField(max_length=150, verbose_name='سایز')),
            ],
            options={
                'verbose_name': 'اطلاعات تکمیلی',
                'verbose_name_plural': ' لیست اطلاعات تکمیلی',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='product_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.productinfo', verbose_name='اطلاعات تکمیلی'),
        ),
    ]
