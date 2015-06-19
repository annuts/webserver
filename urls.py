#!/usr/bin/env python
#conding:utf-8

import tornado.web
from main import MainHandler
from config import settings


app = tornado.web.Application(
    handlers = [
        ('/', MainHandler),
    ],
    **settings
)

