from selenium import webdriver
from time import sleep
import topsecret

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username

        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"] ").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"] ").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"] ").click()
        sleep(4)

        # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
        #     .click()
        # sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(4)

        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()

        sleep(2)


    def get_unfollowers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[1]/div/a/img").click()

        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]") \
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]") \
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)

        scroll_box = self.driver.find_element_by_class_name("isgrP")
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # close button
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names



my_bot = InstaBot('your_username', topsecret.pw())
my_bot.get_unfollowers()