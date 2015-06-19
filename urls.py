#!/usr/bin/env python
#conding:utf-8

import tornado.web
from main import MainHandler

app = tornado.web.Application(
    handlers = [
        ('/', MainHandler),
    ],
)

