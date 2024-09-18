from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.keys import Keys


class SignInPage(PageFactory):

    def __init__(self,driver):
        self.driver = driver

    locators ={
        'user_name':('CSS','#username input'),
        'password':('CSS','#password input'),
        'login_btn':('ID','login-btn')
    }

    def select_username(self,username):
        self.user_name.send_keys(username)

    def select_password(self,password):
        self.password.send_keys(password)

    def click_login(self):
        self.login_btn.click()
