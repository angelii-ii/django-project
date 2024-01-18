from django.db import models

# Create your models here.
from django.utils.text import slugify


class Karbaran(models.Model):
    name=models.CharField(max_length=50)
    lName=models.CharField(max_length=50)
    age=models.IntegerField()
    activity=models.BooleanField()

class ProductCategory(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    url_title=models.CharField(max_length=300)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'

class ProductInfo(models.Model):
    color = models.CharField(max_length=150,verbose_name='رنگ')
    size= models.CharField(max_length=150, verbose_name='سایز')

    def __str__(self):
        return f'{self.color}----{self.size}'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = ' لیست اطلاعات تکمیلی'


class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='تگ')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = ' تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

class Products(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True,verbose_name='دسته بندی')
    product_info=models.OneToOneField(ProductInfo,on_delete=models.CASCADE,null=True,blank=True,verbose_name='اطلاعات تکمیلی')
    product_tag=models.ManyToManyField(ProductTag,verbose_name=' تگ محصول')
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    description=models.CharField(max_length=550)
    popularity=models.BooleanField(verbose_name='فعال/غیرفعال')
    slug=models.SlugField(default='',null=False,db_index=True,unique=True,verbose_name='url')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
