#!/usr/bin/env python
import tornado.web


class MainHandler(tornado.web.RequestHandler):

 def get(self):
        self.write("Hello, world")
