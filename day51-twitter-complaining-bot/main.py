from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import warnings

load_dotenv("../.env")

warnings.filterwarnings("ignore", category=DeprecationWarning)


# /Users/josephbak/Development

PROMISED_DOWN = 300
PROMISED_UP = 300
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
TWITTER_EMAIL = os.getenv("MY_EMAIL")
TWITTER_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

SPEED_TEST_SITE = "https://www.speedtest.net/"
# TWITTER_LOGIN_PAGE = "https://twitter.com/i/flow/login"
TWITTER_LOGIN_PAGE = "https://twitter.com/login"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_SITE)
        sleep(3)

        test_button = self.driver.find_element_by_class_name("start-text")
        test_button.click()

        sleep(50)
        self.up = self.driver.find_element_by_class_name("result-data-large.number.result-data-value.upload-speed").text
        self.down = self.driver.find_element_by_class_name("result-data-large.number.result-data-value.download-speed").text

        print(f"up: {self.up}")
        print(f"down: {self.down}")

        # self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_LOGIN_PAGE)

        sleep(3)
        # email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        # password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        # next_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
        next_button.click()

        sleep(2)

        try:
            user_name = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            user_name.send_keys(TWITTER_USERNAME)

            user_next_botton = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
            user_next_botton.click()
        except Exception as error:
            pass

        sleep(2)

        password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        pw_next_botton = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        pw_next_botton.click()
        sleep(2)
        # password.send_keys(Keys.ENTER)
        #
        sleep(4)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        sleep(3)
        self.driver.quit()


complaining_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
complaining_bot.get_internet_speed()
sleep(5)
if PROMISED_DOWN < complaining_bot.down or PROMISED_UP < complaining_bot.up:
    complaining_bot.tweet_at_provider()