from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class ProductPage(BasePage): 
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
    #     link.click()
    
    # def should_be_login_link(self):
    #     assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"