import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBotChecker:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()
        return

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        return

    def check_followers(self):
        driver = self.driver
        driver.get("https://www.instagram.com/{}".format(self.username))
        time.sleep(2)
        followers_button = driver.find_element_by_xpath("//a[text()=' abonnés']")
        followers_button.click()
        time.sleep(2)
        prev_scroll = 0
        followers = []
        for i in range(1, 100):
            try:
                driver.execute_script("document.getElementsByClassName(\"isgrP\")[0].scrollTo(document.getElementsByClassName(\"isgrP\")[0].scrollTop, {});".format(600 * (i * i)))
                scroll = driver.execute_script("return document.getElementsByClassName(\"isgrP\")[0].scrollHeight;")
                if scroll == prev_scroll:
                    break
                prev_scroll = scroll
                time.sleep(1)
            except Exception:
                continue
        try:
            webelements = driver.find_elements_by_xpath("//div/a[@title]")
            for webelement in webelements:
                followers.append(webelement.text)

        except Exception:
            pass
