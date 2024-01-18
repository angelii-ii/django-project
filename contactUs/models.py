from django.db import models

# Create your models here.

class ContactUs(models.Model):
    title=models.CharField(max_length=300,verbose_name='عنوان')
    email=models.EmailField(max_length=300,verbose_name='ایمیل')
    fullname=models.CharField(max_length=300,verbose_name='نام و نام خانوادگی')
    message=models.TextField(max_length=550,verbose_name='متن پیام')
    date_created=models.DateField(verbose_name='تاریخ ایجاد')
    read_by_admin=models.BooleanField(verbose_name='خوانده شده توسط ادمین',default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='تماس با ما'
        verbose_name_plural='راه های تماس با ما'