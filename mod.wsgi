import os,sys
sys.path.append('/weixin')
os.environ['DJANGO_SETTING_MODULE'] = 'weixin.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
