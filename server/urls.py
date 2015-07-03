#!/usr/bin/env python
#conding:utf-8

import pyrestful.rest
import tornado.web
from main import *
from config import settings


"""
app = tornado.web.Application(
    handlers = [
        ('/', MainHandler),
    ],
    **settings
)
"""

rest_views = [EchoService,]

app = pyrestful.rest.RestService(rest_views)
