import tornado.web
import tornado.ioloop
import Users

application = tornado.web.Application([
    (r"/", Users.Main),
    (r"/login",Users.Login),
    (r"/create" ,Users.SignUp),
    (r"/show",Users.ShowUsers),
],static_path='scripts',debug=True,cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


#(r"/(style\.css)",tornado.web.StaticFileHandler, {"path": "./css/"}),
#(r"/css/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os. path.dirname(__file__), 'css')}),
