from selenium import webdriver
import abc, time, logging, platform, os
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Scrapy(metaclass=abc.ABCMeta):
    def __init__(self):
        self.driver = Scrapy.get_driver()

    def _wait(self, check_token):
        while check_token not in self.driver.find_element_by_xpath('//body').get_attribute('innerHTML'):
            time.sleep(1)
        return

    @staticmethod
    def get_driver():
        options = Scrapy.get_chrome_options()
        if platform.system() == 'Darwin': # Mac
            path = os.path.abspath(os.path.join(__file__, '..', "..", '..', "..", 'chromedriver'))
            driver = webdriver.Chrome(path, options=options)
        else:
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
        options.add_argument("--headless")
        return options

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
