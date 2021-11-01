import time

from selenium import webdriver

bot = webdriver.Chrome(r'C:\Users\user\Documents\Python\daily-tweet\resources\chromedriver.exe')

time.sleep(0.5)

# bot.close()  only closes chrome, not chromedriver.exe

# closes both chrome and chromedriver.exe
bot.quit() 