from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.image import Image

from database import DataBase, Person
from check_correct import check_email, check_number, check_digits

from kivy.config import Config 

Config.set('graphics', 'resizable', '0') # 0 being off 1 being on as in true/false
Config.set('graphics', 'width', '1100') # fix the width of the window  
Config.set('graphics', 'height', '650') # fix the height of the window

class Email_User:
    def __init__(self):
        self.email_addr = ""
        self.id_num = ""

    def set_email_adrr(self, emaill):
        self.email_addr = emaill

    def get_email_adrr(self):
        return self.email_addr

    def set_idd(self, iddd):
        self.id_num = iddd

    def get_idd(self):
        return self.id_num

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None) #password is the id number
    phone_number = ObjectProperty(None)

    def submit(self):
        if ((check_email(self.email.text) > 0) and (check_number(self.phone_number.text) > 0)):
            if self.password != "":
                exist = db.add_user(self.namee.text, self.password.text, self.email.text, self.phone_number.text)
                if (exist==(-1)):
                    emailexists()
                else:
                    self.reset()
                    sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        self.phone_number.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None) #password is the id number

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            eu.set_email_adrr(self.email.text)
            eu.set_idd(self.password.text)
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    num_shoot1 = ObjectProperty(None)
    num_shoot2 = ObjectProperty(None)
    num_shoot3 = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def target1(self):
        if (check_digits(self.num_shoot1.text) == 1):
            db.activate_target_image_process(eu.get_email_adrr(), "1", self.num_shoot1.text)
            done()
        else:
            invalidForm()

    def target2(self):
        if (check_digits(self.num_shoot2.text) == 1):
            db.activate_target_image_process(eu.get_email_adrr(), "2", self.num_shoot2.text)
            done()
        else:
            invalidForm()

    def target3(self):
        if (check_digits(self.num_shoot3.text) == 1):
            db.activate_target_image_process(eu.get_email_adrr(), "3", self.num_shoot3.text)
            done()
        else:
            invalidForm()

    def new_clean_target(self):
        db.new_target_picture()
    
    def send_me_statistics(self):
        check_success = db.send_statistics(eu.get_email_adrr())
        if check_success == (-1):
            No_statistics()

    def remove_user(self):
        db.remove_dir(eu.get_email_adrr(), eu.get_idd())
        sm.current = "login" 

    def on_enter(self, *args):
        pass
        #self.n.text = "Account Name: " + (users_db.get_user(n).get_name())
        #self.email.text = "Email: " + (users_db.get_user(email).get_name())
        #self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def emailexists():
    pop = Popup(title='Email exists',
                  content=Label(text='Email already exists.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def No_statistics():
    pop = Popup(title='No_statistics',
                  content=Label(text='There are not enough images to create statistics.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def done():
    pop = Popup(title='Done',
                  content=Label(text='Done!'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase()
eu = Email_User()

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()