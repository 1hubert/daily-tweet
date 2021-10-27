import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# preparing the options for the chrome driver
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
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Chrome('./resources/chromedriver.exe', options=options)

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

    def twitter_like(self, hashtag):
        bot = self.bot
        heart_count = 0
        #bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        bot.get('https://twitter.com/' + hashtag)
        time.sleep(4)
        for _ in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3) # 2
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link) # maybe / is missing idk
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    heart_count += 1
                    #print('Beep Bop! I already liked ' + heart_count + ' different posts!')
                    time.sleep(3)
                except Exception:
                    time.sleep(60)

    def post(self):
        pass

    def like_your_own_post(self):
        pass


jg = TwitterBot('jaroslawgyro4@gmail.com', 'Hub123!@#')
jg.login()
    
