import re
import pyautogui
import pandas as pd
import argparse
from datetime import datetime
from random import randint
from time import sleep
from selenium import webdriver


ap = argparse.ArgumentParser()
ap.add_argument("-l", "--listhashtags", required=True,
	help="hashtags separeted by a comma (,)")
ap.add_argument("-n", "--numofposts", required=True,
	help="number of posts to like")

args = vars(ap.parse_args())

if args["listhashtags"]:
	hashtag_list = args["listhashtags"].split(",")
if args["numofposts"]:
	num_of_posts = int(args["numofposts"])

now = datetime.now()
driver = webdriver.Chrome()

username = "shah_jahan.captures"
password = "<password>"

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

	print("[INFO] Successfully logged in.")

	sleep(1)



def go_to_tag(driver, hashtag):

	driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
	print(f"[INFO] At hashtag: {hashtag}")

	sleep(5)
		

def click_on_first_thumbnail(driver):
	first_thumbnail_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]")
	first_thumbnail_button.click()
	sleep(2)

def check_likes_on_post(driver):
	try:
		likes_on_post_button = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d     _8A5w5    ']")
		likes_on_post_html = likes_on_post_button.get_attribute("innerHTML")
		#print(likes_on_post_html)
		likes_on_post = re.findall(r'<span>(.+?)</span>', likes_on_post_html)
		#print(likes_on_post)
		if (likes_on_post != [] and int(likes_on_post[0]) <= 999) or likes_on_post_html == "1 like" or likes_on_post_html == "like this" or likes_on_post_html == "Following":
			print("[INFO] Likes on post <= 999")
			return True
		else:
			print("[INFO] Likes on post > 999")
			return False
	except:
		pass


def like_post(driver):
	#like_button = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg")
	like_button = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
	like_button.click()
	print("[INFO] Liked a post.")

	sleep(2)


def comment_on_post(driver, post):
	user_handle = driver.find_element_by_xpath("//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV '][@tabindex='0']").get_attribute("innerHTML")

	comments_list = ['What an attractive picture!', 'What a pretty picture!', 'What a handsome picture!', 'What a good-looking picture!', 'What a nice-looking picture!', 'What a pleasing picture!', 'What an alluring picture!', 'What a prepossessing picture!', 'What a lovely picture!', 'What a charming picture!', 'What a delightful picture!', 'What an appealing picture!', 'What an engaging picture!', 'What a winsome picture!', 'What a ravishing picture!', 'What a gorgeous picture!', 'What a heavenly picture!', 'What a stunning picture!', 'What an arresting picture!', 'What a glamorous picture!', 'What an irresistible picture!', 'What a bewitching picture!', 'What a beguiling picture!', 'What a graceful picture!', 'What an elegant picture!', 'What an exquisite picture!', 'What an aesthetic picture!', 'What an artistic picture!', 'What a decorative picture!', 'What a magnificent picture!', 'What an amazing picture!', 'What an astonishing picture!', 'What a staggering picture!', 'What a shocking picture!', 'What a surprising picture!', 'What a breathtaking picture!', 'What a striking picture!', 'What an impressive picture!', 'What a bewildering picture!', 'What a stunning picture!', 'What a stupefying picture!', 'What an unnerving picture!', 'What an unsettling picture!', 'What a disturbing picture!', 'What a disquieting picture!', 'What an awe-inspiring picture!', 'What a remarkable picture!', 'What a notable picture!', 'What a noteworthy picture!', 'What an extraordinary picture!', 'What an outstanding picture!', 'What an incredible picture!', 'What an unbelievable picture!', 'What a phenomenal picture!', 'What an exceptional picture!', 'What an extraordinary picture!', 'What a remarkable picture!', 'What an outstanding picture!', 'What an amazing picture!', 'What an astonishing picture!', 'What an astounding picture!', 'What a stunning picture!', 'What a staggering picture!', 'What a marvellous picture!', 'What a magnificent picture!', 'What a wonderful picture!', 'What a sensational picture!', 'What a breathtaking picture!', 'What a miraculous picture!', 'What a singular picture!', 'What an incredible picture!', 'What an unbelievable picture!', 'What an inconceivable picture!', 'What an unimaginable picture!', 'What an uncommon picture!', 'What an unheard of picture!', 'What an unique picture!', 'What an unparalleled picture!', 'What an unprecedented picture!', 'What an unusual picture!', 'What an unusually good picture!', 'What a too good to be true picture!', 'What a superlative picture!', 'What a prodigious picture!', 'What a surpassing picture!', 'What a rare picture!', 'What a fantastic picture!', 'What a fabulous picture!', 'What a stupendous picture!', 'What an out of this world picture!', 'What a terrific picture!', 'What a tremendous picture!', 'What a brilliant picture!', 'What a mind-boggling picture!', 'What a mind-blowing picture!', 'What an awesome picture!', 'What a stellar picture!', 'What a wondrous picture!']
	comment_random = randint(1,len(comments_list)-2)
	comment = comments_list[comment_random]
	comment = user_handle + " , " + comment



	if post%2 == 0:
		try:
			comment_input = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea")
		except:
			if driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.MhyEU > div").get_attribute("innerHTML") == "Comments on this post have been limited.":
				print("[INFO] Comments limited.")
		try: 
			comment_input.send_keys(comment)
			print("[INFO] Commented on a post.")
		except:
			pyautogui.typewrite(comment)
			pyautogui.press('enter')
			print("[INFO] Commented on a post.")
			sleep(18)
	elif post % 2 != 0:
		print("[INFO] No comment.")
	
	else:
		print("[INFO] No comment.")
		sleep(1)


def follow_person(driver):
	follow_button = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button")
	if follow_button.get_attribute("innerHTML") == "Follow":
		follow_button.click()
		print("[INFO] Followed a person.")

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
	followed_users_df.to_csv(f'new_following_log/{now.strftime("%Y%m%d-%H%M%S")}_users_followed_list.csv')
	print("\n[INFO] Created a csv file of followed users.")

def main(driver, hashtag_list, num_of_posts):

	likes = 0
	comments = 0
	follows = 0

	followed_users = []

	login(driver, username, password)

	for hashtag in hashtag_list:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		go_to_tag(driver, hashtag)

		click_on_first_thumbnail(driver)

		for post in range(num_of_posts):
			print("-----------------------------------")
			try:
				if check_likes_on_post(driver):

					like_post(driver)
					likes += 1
					
					follow_person(driver)
					follows += 1
					
					# Commenting
					comment_on_post(driver, post)
					comments += 1

					#Getting and storing user handle
					followed_users.append(get_user_handle(driver))

				else:
					sleep(1)
			except:
				pass
			go_to_next_post(driver)

	create_df_csv(followed_users)

	sleep(5)
	driver.close()

	print(f"\n[INFO] Liked {likes} posts")
	print(f"[INFO] Commented on {comments} posts")
	print(f"[INFO] Followed {follows} people")

main(driver, hashtag_list, num_of_posts)
