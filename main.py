import selenium
import telebot
import time
import  random
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua = UserAgent()
mail = ['']
password = ['']
a = 0
c = ['явахуи','Боже что за кринж...','Подписуюсь взаимно!','Ха, ЖИЗА','Есть кто-то из украины?','ЯВАХУИ','Кстати я дед инсайд','Я какаю и никто об этом не узнает',
	'Кто взаимную подписку?']
opts = Options()
ua = UserAgent()
opts.add_argument('headless')
opts.add_argument('--no-sandbox')
opts.add_argument(f"user-agent={ua.opera}")
chromedriver = ''
#options.headless = True
browser = webdriver.Chrome(chromedriver,options=opts)
def main():
	browser.get('https://www.tiktok.com/login/phone-or-email/email')
	#login
	time.sleep(1)
	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input').send_keys(mail[0])
	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input').send_keys(password[0])
	browser.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/button').click()
	browser.find_element(By.XPATH, '//div[@class="tiktok-1lh5noh-DivVideoCardContainer e1bh0wg77"]').click()
	input('')
	while True:
		try:#like and subscribe
			time.sleep(1)
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]').click()
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[1]/button').click()
			browser.find_element(By.XPATH, '//*[@id="placeholder-f781i"]').send_keys('Подпишусь взаимно!')
			like_count = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]/strong').text()
			print(like_count)
			browser.find_element(By.XPATH, '//*[@id="placeholder-539dk"]').send_keys(random.choice(c))
			time.sleep(15)
			browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/button[3]').click()
		except Exception as e:
			print(e)


	a+=1
main()
