import tornado.ioloop
import tornado.web
from connectDB import _execute


class Main(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        username = self.current_user
        self.render('templates/index.html')
        return username


# Sign Up
class SignUp(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/signUp.html')

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("pass")

        select = ''' select name from users where name = '%s' ''' % (name);
        res = _execute(select)

        if len(res) == 0:
            query = ''' insert into users (name , password) values (%s , %s) ''' % ( "'" + name + "'", "'" + password + "'");
            print(query)
            _execute(query)
            self.render('templates/login.html')

        else:
            self.write("Sorry, Duplicated name, please enter another name !")
        self.render('templates/signUp.html')

# Login
class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/login.html')

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("pass")
        self.set_secure_cookie("name", name[1])

        query = ''' select name from users where name = '%s' and password = '%s' ''' % (name,password);
        res = _execute(query)

        if len(res) == 0:
            self.write("Incorrect Username or Password!!")
            self.render('templates/login.html')

        else:
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")

#logout
class Logout(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("name")
        self.redirect("/")


#select all users
class ShowUsers(tornado.web.RequestHandler):
    def get(self):
        query = ''' select * from users '''
        rows = _execute(query)
        self._processresponse(rows)

    def _processresponse(self,rows):
        self.write("<b>Records</b> <br /><br />")
        for row in rows:
                self.write(str(row[0]) + "      " + str(row[1]) +" <br />" )
