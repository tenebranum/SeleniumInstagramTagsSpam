from .credits import login, password 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import ast
import random


with open('accs.txt') as f:
    accs = f.read()
    accs = ast.literal_eval(accs)
iterator = 0
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.instagram.com/accounts/login/?next=%2Fp%2FB1lkxVJCArl%2F&source=logged_out_half_sheet")
time.sleep(2)
username = driver.find_element_by_xpath('//*[@name="username"]')
password = driver.find_element_by_xpath('//*[@name="password"]')
username.send_keys(login)
password.send_keys(password)
password.submit()
time.sleep(1200)
while iterator < 3000:
	succ = False
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	comment = driver.find_element_by_xpath('//*[@class="Ypffh"]')
	action = ActionChains(driver)
	action.move_to_element(comment)
	action.click_and_hold()
	action.perform()
	time.sleep(5)
	try:
		for i in range(3):
			if not succ:
				comment = driver.find_element_by_xpath('//*[@class="Ypffh"]')
				comment.send_keys('{}{} '.format('@', accs[iterator]))
				succ = True
	except:
		time.sleep(2)
	comment.submit()
	while comment.text:
		comment.submit()
		time.sleep(120)
	iterator += 1
	print(iterator)
	sleep_period = 170 + random.randint(10, 25)
	time.sleep(sleep_period)

