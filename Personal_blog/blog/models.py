from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible


# Create your models here.
class Category(models.Model): #分类
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):    #标签
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):    #文章
    #文章标题
    title=models.CharField(max_length=70)
    #文章正文
    body=models.TextField()
    #文章创建时间
    created_time=models.DateTimeField()
    #文章最后一次修改时间
    modified_time=models.DateTimeField()
    #文章摘要，可为空
    excerpt=models.CharField(max_length=200,blank=True)
    
    #关联三个表
    category=models.ForeignKey(Category)#一对多
    tags=models.ManyToManyField(Tag,blank=True)#多对多
    author=models.ForeignKey(User)#django内置
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time']
