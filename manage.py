import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = template.Loader("/home/serhii/Tornado/website/venv/webproject")
        loader.load('index.html')

def make_app():
    app = tornado.web.Application([
        (r"/", MainHandler)
    ])
    return app

def daemon(iport):
    http_server = make_app()
    http_server.listen(iport, "localhost")
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    daemon(8008)