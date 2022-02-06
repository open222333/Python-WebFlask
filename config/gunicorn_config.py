# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function
import multiprocessing

bind = ['0.0.0.0:5000', '[::1]:5000']
workers = max((multiprocessing.cpu_count() * 2) - 1, 2)
worker_class = 'gevent'
# loglevel = 'error'
accesslog = '-'
errorlog = '-'
forwarded_allow_ips = '*'
x_forwarded_for_header = 'X-FORWARDED-FOR'
# secure_scheme_headers = {
#    'X-FORWARDED-PROTO': 'https',
# }
timeout = 300
