from django.core.handlers.wsgi import WSGIHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer
from sockjs.tornado import SockJSRouter

from MyWebChat.chat import SocketHandler

define('port', type=int, default=8888)
wsgi_app = WSGIContainer(WSGIHandler())
tornado_app = Application(SockJSRouter(SocketHandler, '/sock').urls + [
    ('.*', FallbackHandler, dict(fallback=wsgi_app),)])
server = HTTPServer(tornado_app)
server.listen(options.port)
print('listening:' + str(options.port))
IOLoop.instance().start()