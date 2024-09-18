from selenium import webdriver
from src.pages.sign_up_page import SignInPage
from src.pages.homepage import Homepage
import time

def test_sign_in():
    driver = webdriver.Chrome()
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)


    homepage.click_sign_in()
    print(f'Sign in button is clicked')

    time.sleep(2)

    sign_in_page.select_username('demouser\n')
    sign_in_page.select_password('testingisfun99\n')
    sign_in_page.click_login()

    time.sleep(2)

    homepage.get_username()

    time.sleep(5)

    driver.quit()