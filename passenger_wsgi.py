# -*- coding: utf-8 -*-
import os, sys
sys.path.append('/home/t/timofeaa/tt-main/ttmainsite')
sys.path.append('/home/t/timofeaa/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ttmainsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
