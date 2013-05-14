import os, sys
import django.core.handlers.wsgi

sys.path.append('C://Server//Apache2.2//htdocs')

os.environ['DJANGO_SETTINGS_MODULE'] = 'weixin.settings'
application = django.core.handlers.wsgi.WSGIHandler()
