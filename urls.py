# coding=utf-8
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from weixin.autore.views import handle_request
#调用路径解析微信模块
from django.conf import settings
#解析上传的静态图片文件
from weixin.autore.views import news_list
#调用路径解析新闻模块


urlpatterns = patterns('',
    # Example:
    # (r'^weixin/', include('weixin.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root), #解析自动生成的Admin目录
    (r'^wx$',handle_request), #调用路径解析微信模块
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name="media"),
    #解析上传的静态图片文件
    (r'^news/$', news_list), #调用路径解析新闻模块
    (r'^tinymce/', include('tinymce.urls')), #调用tinymce富文本模块
    #安装参考 django-tinymce 项目，根据提示信息需要把tiny_mce模块拷贝到media目录下的js目录下，可以参考404信息
    )