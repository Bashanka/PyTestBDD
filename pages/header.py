from enum import Enum
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Locators(Enum):
    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    ACCOUNT_LABEL = (By.CLASS_NAME, "account")


class Header:

    def __init__(self, browser):
        self.bp = BasePage(browser)

    def click_sign_in(self):
        self.bp.click(*Locators.SIGN_IN_BUTTON.value)

    def get_account_name(self):
        return self.bp.get_text(*Locators.ACCOUNT_LABEL.value)
