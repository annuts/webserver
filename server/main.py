#!/usr/bin/env python
import tornado.web
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get

"""
class MainHandler(tornado.web.RequestHandler):

 def get(self):
        self.write("Hello, world")
"""

class EchoService(pyrestful.rest.RestHandler):
    @get(_path="/api/{name}", _produces=mediatypes.APPLICATION_JSON)
    def sayHello(self, name):
	print name
	return {"Hello": name}
