from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag         #最新文章模板标签
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag          #归档模板标签 
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag    
def get_categories():         #分类模板标签
    return Category.objects.all()
    
    
