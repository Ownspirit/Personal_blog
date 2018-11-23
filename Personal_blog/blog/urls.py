from django.conf.urls import url
from . import views       #从当前目录下导入views模块

app_name= 'blog'
urlpatterns=[
    url(r'^$',views.index,name='index'), #第一个参数是网址（正则表达式），第二个参数是处理函数，最后一个参数是函数别名
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]
