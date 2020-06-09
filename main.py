#follow and like with hashtags
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import random

insta_id = ""
insta_password = ""
clock = random.randint(2, 4)


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.instagram.com')

def login():
	usr_name = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(insta_id)
	pass_word = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(insta_password)
	login_btn = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
	

def entry_noti():
	try:
		btn = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
		btn.click()
	except:
		browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
		browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()


def like_follow():
	#hashtag list
	hash_tag = ["newyork"]
	for k in hash_tag:#loop to run all hash tags
		#navigation to hashtag
		browser.get('https://www.instagram.com/explore/tags/'+k+'/')
		#selecting the first recent post
		browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]').click()
		for i in range(10):
			time.sleep(clock)
			try:
			    #like button
			    browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
			    time.sleep(clock)
			    #follow button
			    browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
			    time.sleep(clock)
				#next button
			    browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
			except:
				browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
				time.sleep(1)
				browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
				time.sleep(1)
				browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()

				



		
		
time.sleep(2)
login()

time.sleep(3)
entry_noti()

time.sleep(clock)
like_follow()
