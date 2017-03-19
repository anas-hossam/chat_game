import tornado.web
import tornado.ioloop
import Users

application = tornado.web.Application([
    (r"/", Users.Main),
    (r"/login",Users.Login),
    (r"/create" ,Users.SignUp),
    (r"/show",Users.ShowUsers),
],static_path='scripts',debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()