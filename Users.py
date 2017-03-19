import tornado.ioloop
import tornado.web
from connectDB import _execute


class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("Main")


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
            # query = ''' insert into users (name , password) values (%s , %s) ''' % (name , password );
            print(query)
            _execute(query)
            self.render('templates/index.html')
            # self.redirect('templates/index.html')

        else:
            self.write("Sorry, Duplicated name, please enter another name !")

# Login
class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/login.html')

    def post(self):
        name = self.get_argument("name")
        password = self.get_argument("pass")

        selectLogin = ''' select name from users where name = '%s' ''' % (name);
        res = _execute(selectLogin)
        print("login fun")

        if len(res) == 0:
            self.write("success")
            # self.render('templates/index.html')

        else:
            self.write("Incorrect Data!!")


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