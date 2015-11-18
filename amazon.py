import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
import page
import todaysdeals

class Amazon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_methods(self):
        main_page = page.MainPage(self.driver)
        main_page.test_load_amazon_page()
        todaysdeals_page = todaysdeals.MainPage(self.driver)
        todaysdeals_page.test_check_todays_deals()
        todaysdeals_page.test_add_to_cart()
        todaysdeals_page.test_check_cart()
        todaysdeals_page.test_count_items()

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()

