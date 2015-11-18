from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class BasePage(object):
        
        def __init__(self, driver):
                self.driver = driver


class MainPage(BasePage):

        def test_load_amazon_page(self):
                driver = self.driver
                driver.get("https://www.amazon.com")
               
