import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

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
        bot.get('https://twitter.com/i/flow/login')
        time.sleep(4)

        email = bot.find_element_by_tag_name('input')
        email.clear()  # Just in case
        email.send_keys(self.email)
        time.sleep(1)
        next = bot.find_elements_by_css_selector('[role="button"]')[2]
        next.click()
        time.sleep(2)

        try:
            your_name_here = bot.find_element_by_css_selector('[inputmode="text"]')
            your_name_here.send_keys('GyroZep27172727')
            time.sleep(0.2)
            next = bot.find_elements_by_css_selector('[role="button"]')[2]
            next.click()
            time.sleep(2)
        except NoSuchElementException:
            pass
        
        password = bot.find_elements_by_tag_name('input')[1]
        password.clear()
        password.send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_css_selector('[data-testid="LoginForm_Login_Button"]').click()
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


print()
print()
print()
print()
print()
jg = TwitterBot('jaroslawgyro4@gmail.com', 'Hub123!@#')
jg.login()
    
