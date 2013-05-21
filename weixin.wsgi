# coding=utf-8
import os, sys
import django.core.handlers.wsgi

sys.path.append('C://Server//Apache2.2//htdocs')
#添加解析主目录

os.environ['DJANGO_SETTINGS_MODULE'] = 'weixin.settings'
#声明主目录配置信息文件位置
application = django.core.handlers.wsgi.WSGIHandler()
