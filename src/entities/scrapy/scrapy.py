from selenium import webdriver
import abc, time, logging
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import abc


class Scrapy(metaclass=abc.ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_driver():
        options = Scrapy.get_chrome_options()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0,
        #          'download.default_directory': self.save_path,
        #          'directory_upgrade': True}
        # options.add_experimental_option('prefs', prefs)

        # hide the web driver window
        #options.add_argument("--headless")
        return options

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()