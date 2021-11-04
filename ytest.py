
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys
from docx import Document
import time
import pytest


class buttons():
    video_ViewCount_class = 'style-scope ytd-video-meta-block'
    video_Title_id = 'video-title'




class Youtube(buttons):
    def test_loop(self):
        self.launcher()
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.view_Count()
        self.filter()
        self.driver.quit()

    def view_Count(self):
        self.views = []
        total = self.driver.find_elements_by_class_name(buttons.video_ViewCount_class)
        for i in total:
            self.views.append(i.text)

    def filter(self):
        watchers = []
        for i in self.views:
            new = i.split('\n')
            print(new)
            if len(new) > 1:
                watchers.append(new[1])
        print(watchers)

    def click_Random_Video(self):
        self.driver.find_element_by_id(buttons.video_Title_id)

    def launcher(self):
        # Launching chrome with the extention
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('https://www.youtube.com/')

    def test_method(self):
        self.driver.close()
        self.driver.quit()



tester = Youtube()
tester.test_loop()