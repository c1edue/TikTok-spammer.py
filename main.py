import selenium
import telebot
import time
import random
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua = UserAgent()
mail = ['c1edue.dtt@gmail.com']
password = ['Aabbcc132*']
opts = Options()
opts.add_argument("--disable-blink-features=AutomationControlled")
#opts.add_argument('headless')
opts.add_argument(f"user-agent={ua.random}")
chromedriver = 'chromedriver.exe'
dt = datetime.datetime.now()
print(dt)
#options.headless = True
browser = webdriver.Chrome(chromedriver,options=opts)
def main():
	a=0
#	browser.get('https://www.tiktok.com/login/phone-or-email/email')
	#login
#	time.sleep(1)
#	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input').send_keys(mail[0])
#	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input').send_keys(password[0])
#	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button').click()
	input('')
	browser.find_element(By.XPATH, '//div[@class="tiktok-1lh5noh-DivVideoCardContainer e1bh0wg77"]').click()

	while True:
		dt = datetime.datetime.now()
		a+=1
		try:#like and subscribe
			time.sleep(1)
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
			time.sleep(2)
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[1]/button').click()
			time.sleep(5)
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/button[3]').click()
			print(f'Lap: {a} \n{dt} ')
			time.sleep(20)

		except Exception as e:
			print(e)


	a+=1
main()
