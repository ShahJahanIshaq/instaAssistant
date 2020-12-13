import re
import pyautogui
import pandas as pd
from datetime import datetime
from random import randint
from time import sleep
from selenium import webdriver

now = datetime.now()
driver = webdriver.Chrome()



def login(driver, username, password):

	driver.implicitly_wait(5)

	driver.get('https://www.instagram.com/')

	username_input = driver.find_element_by_css_selector("input[name='username']")
	password_input = driver.find_element_by_css_selector("input[name='password']")

	username_input.send_keys(username)
	password_input.send_keys(password)

	login_button = driver.find_element_by_xpath("//button[@type='submit']")
	login_button.click()

	sleep(2)

	notnow_button = driver.find_element_by_xpath("//button[text()='Not Now']")
	notnow_button.click()

	sleep(2)

	notnow_button_2 = driver.find_element_by_xpath("//button[text()='Not Now']")
	notnow_button_2.click()

	sleep(1)



def go_to_tag(driver, hashtag):

	driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

	sleep(5)
		

def click_on_first_thumbnail(driver):
	first_thumbnail_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")
	first_thumbnail_button.click()
	sleep(2)

def check_likes_on_post(driver):
	likes_on_post_button = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d     _8A5w5    ']")
	likes_on_post_html = likes_on_post_button.get_attribute("innerHTML")
	print(likes_on_post_html)
	likes_on_post = re.findall(r'<span>(.+?)</span>', likes_on_post_html)
	print(likes_on_post)
	if (likes_on_post != [] and int(likes_on_post[0]) <= 999) or likes_on_post_html == "1 like" or likes_on_post_html == "like this":
		return True
	else:
		return False

def like_post(driver):
	#like_button = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg")
	like_button = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
	like_button.click()

	sleep(2)


def comment_on_post(driver):
	user_handle = driver.find_element_by_xpath("//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV '][@tabindex='0']")

	comments_list = ['What an attractive picture!', 'What a pretty picture!', 'What a handsome picture!', 'What a good-looking picture!', 'What a nice-looking picture!', 'What a pleasing picture!', 'What an alluring picture!', 'What a prepossessing picture!', 'What a lovely picture!', 'What a charming picture!', 'What a delightful picture!', 'What an appealing picture!', 'What an engaging picture!', 'What a winsome picture!', 'What a ravishing picture!', 'What a gorgeous picture!', 'What a heavenly picture!', 'What a stunning picture!', 'What an arresting picture!', 'What a glamorous picture!', 'What an irresistible picture!', 'What a bewitching picture!', 'What a beguiling picture!', 'What a graceful picture!', 'What an elegant picture!', 'What an exquisite picture!', 'What an aesthetic picture!', 'What an artistic picture!', 'What a decorative picture!', 'What a magnificent picture!', 'What an amazing picture!', 'What an astonishing picture!', 'What a staggering picture!', 'What a shocking picture!', 'What a surprising picture!', 'What a breathtaking picture!', 'What a striking picture!', 'What an impressive picture!', 'What a bewildering picture!', 'What a stunning picture!', 'What a stupefying picture!', 'What an unnerving picture!', 'What an unsettling picture!', 'What a disturbing picture!', 'What a disquieting picture!', 'What an awe-inspiring picture!', 'What a remarkable picture!', 'What a notable picture!', 'What a noteworthy picture!', 'What an extraordinary picture!', 'What an outstanding picture!', 'What an incredible picture!', 'What an unbelievable picture!', 'What a phenomenal picture!']
	comment_random = randint(1,len(comments_list))
	comment = comments_list[comment_random]
	comment = user_handle + ", "

	if driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea") and post%3==0:

		comment_input = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea")
		try: 
			comment_input.send_keys(comment)
		except:
			pyautogui.typewrite(comment)
			pyautogui.press('enter')
			sleep(10)
	else:
		sleep(1)

def follow_person(driver):
	follow_button = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
	if follow_button.get_attribute("innerHTML") == "Follow":
		follow_button.click()

		sleep(1)

def get_user_handle(driver):
	user_handle_link = driver.find_element_by_xpath("//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV '][@tabindex='0']")
	user_handle = user_handle_link.get_attribute("innerHTML")

	return user_handle

def go_to_next_post(driver):
	driver.find_element_by_link_text('Next').click()
	sleep(4)

def create_df_csv(users_list):
	followed_users_df = pd.DataFrame(users_list)
	followed_users_df.to_csv(f'{now.strftime("%Y%m%d-%H%M%S")}_users_followed_list.csv')

def main(driver, hashtag_list, num_of_posts):

	likes = 0
	comments = 0
	follows = 0

	followed_users = []

	login(driver, 'shah_jahan.captures', '3Bscdeop3')

	for hashtag in hashtag_list:

		go_to_tag(driver, hashtag)

		click_on_first_thumbnail(driver)

		for post in range(num_of_posts):
			
			if check_likes_on_post(driver):

				like_post(driver)
				likes += 1
				
				follow_person(driver)
				follows += 1
				
				#Commenting
				# comment_on_post(driver)
				# comments += 1

				#Getting and storing user handle
				followed_users.append(get_user_handle(driver))

			else:
				sleep(1)

			go_to_next_post(driver)

	create_df_csv(followed_users)

	sleep(5)
	driver.close()

	print()
	print(f"Liked {likes} posts")
	print(f"Commented on {comments} posts")
	print(f"Followed {follows} people")

main(driver, ["photographydaily", "ig_shotz"], 1)