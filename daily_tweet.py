import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TwitterBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome('./resources/chromedriver.exe')

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(2)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()  # Just in case
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def post(self):
        pass

    def like_your_own_post(self):
        pass


jg = TwitterBot('jaroslawgyro4@gmail.com', 'Hub123!@#')

    
