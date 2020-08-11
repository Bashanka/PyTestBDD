from enum import Enum
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Locators(Enum):
    EMAIL_CREATE = (By.ID, "email_create")
    SUBMIT_CREATE = (By.ID, "SubmitCreate")


class SignInPage:

    def __init__(self, browser):
        self.bp = BasePage(browser)

    def input_email_create(self, text):
        self.bp.input_text(*Locators.EMAIL_CREATE.value, text)

    def click_create_button(self):
        self.bp.click(*Locators.SUBMIT_CREATE.value)
