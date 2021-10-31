import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from random_mandelbrot_zoom import mandelbrot

script_location = os.path.dirname(__file__)

# Preparing the options for the chrome driver
options = webdriver.ChromeOptions()
#options.add_argument("headless")
options.add_argument("--mute-audio")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--ignore-certificate-errors")
options.add_argument("log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class TwitterBot:
    def __init__(self, email, password, user_tag):
        self.email = email
        self.password = password
        self.user_tag = user_tag
        self.bot = webdriver.Chrome(script_location + '\\resources\\chromedriver.exe', options=options)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(3.5)

        email = bot.find_element_by_tag_name('input')
        email.clear()
        email.send_keys(self.email)
        time.sleep(1)
        next = bot.find_elements_by_css_selector('[role="button"]')[2]
        next.click()
        time.sleep(1)

        try:
            your_name_here = bot.find_element_by_css_selector('[inputmode="text"]')
            your_name_here.send_keys(self.user_tag)
            time.sleep(0.2)
            next = bot.find_elements_by_css_selector('[role="button"]')[2]
            next.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        
        password = bot.find_elements_by_tag_name('input')[1]
        password.clear()
        password.send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_css_selector('[data-testid="LoginForm_Login_Button"]').click()
        time.sleep(2)

    def twitter_like(self, user_tag_to_like):
        bot = self.bot
        heart_count = 0
        bot.get('https://twitter.com/' + user_tag_to_like)
        time.sleep(4)

        for _ in range(10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)

        tweets = bot.find_elements_by_css_selector('[role="link"]')

        links=[]
        for elem in tweets:
            elem = elem.get_attribute('href')
            if 'status' in elem and '/photo' not in elem and elem not in links:
                links.append(elem)

        for link in links:
            print("link: ", link)
            bot.get(link)
            time.sleep(3.5)
            try:
                bot.find_element_by_css_selector('[aria-label="Like"]').click()
                heart_count += 1
                print('Liked ', heart_count, ' different posts from user ', user_tag_to_like)
            except NoSuchElementException:
                print("This post has already been liked by this account or there is no such element")

    def post(self, text=None, media_path=None):
        bot = self.bot

        if bot.current_url != 'https://twitter.com/home':
            bot.get('https://twitter.com/home')
            time.sleep(2)

        if text:
            whats_happening = bot.find_element_by_css_selector('[class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
            whats_happening.send_keys(text)

        if media_path:
            media_button = bot.find_element_by_css_selector('[accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"]')
            media_button.send_keys(media_path)

        time.sleep(0.5)
        send_button = bot.find_element_by_css_selector('[data-testid="tweetButtonInline"]')
        send_button.click()
        time.sleep(2)

    def close(self):
        self.bot.close()


def post_every_x_seconds_y_times(twitter_bot_object, x, y):
    for i in range(y):
        twitter_bot_object.post(media_path=script_location+'\\images\\img' + str(i + 1) + '.png')
        time.sleep(x)


def post_every_x_hours_y_times(twitter_bot_object, x, y):
    time_in_seconds = x * 60 * 60
    for i in range(y):
        twitter_bot_object.post(media_path=script_location+'\\images\\img' + str(i + 1) + '.png')
        time.sleep(time_in_seconds)


def post_random_mandelbrot_zoom(twitter_bot_object):
    mandelbrot()
    path_to_mandelbrot_image = script_location + '\\images\\mandelbrot.png'
    twitter_bot_object.post(media_path=path_to_mandelbrot_image)
    os.remove(path_to_mandelbrot_image)


with open(script_location + '\\twitter_login_credentials.txt', 'r') as f:
    login_credentials = f.read().splitlines()

email = login_credentials[0]
password = login_credentials[1]
user_tag = login_credentials[2]

jg = TwitterBot(email, password, user_tag)
jg.login()
post_random_mandelbrot_zoom(jg)
jg.close()