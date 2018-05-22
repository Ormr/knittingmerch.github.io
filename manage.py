import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url("story", "1"))

class StoryHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)

def make_app():
    app = Application([
        (r"/", MainHandler),
        (r"/story/([0-9]+)", StoryHandler, name="story")
    ])
    return app

def daemon(iport):
    http_server = make_app()
    http_server.listen(iport, "localhost")
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    daemon(8008)