from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(driver, 3000)
        global deal_title


class MainPage(BasePage):

    def test_check_todays_deals(self):
        driver = self.driver
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Today's Deals'))).click()


    def test_add_to_cart(self):
        driver = self.driver
        waste_king = wait.until(EC.visibility_of_element_located((By.ID, '')))
        actions = new Actions(driver)
        actions.move_to_element(waste_king)
        actions.perform()
        deal_title = driver.find_element_by_id('dealTitle').text()
        driver.find_element_by_id('dealActionButton').click()

    def test_check_cart(self):
        driver = self.driver
        wait.until(EC.visibility_of_element_located((By.ID, ''))).click()
        cart_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '')
        cart_item_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ''))).text()
        assert cart_item_title == deal_title

    def test_count_items(self):
        cart_count = driver.find_element_by_id('').text
        count = driver.find_element_by_id('').text
        assert cart_count == count driver = self.driver
                                                     
                                                     

        
