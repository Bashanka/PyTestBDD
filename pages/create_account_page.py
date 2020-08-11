from enum import Enum
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class Locators(Enum):
    YPI_MR_RADIO_BUTTON = (By.ID, "id_gender1")
    YPI_MRS_RADIO_BUTTON = (By.ID, "id_gender2")
    YPI_FIRSTNAME_INPUT = (By.ID, "customer_firstname")
    YPI_LASTNAME_INPUT = (By.ID, "customer_lastname")
    YPI_EMAIL_INPUT = (By.ID, "email")
    YPI_PASSWORD_INPUT = (By.ID, "passwd")

    YA_FIRSTNAME_INPUT = (By.ID, "firstname")
    YA_LASTNAME_INPUT = (By.ID, "lastname")
    YA_COMPANY_INPUT = (By.ID, "company")
    YA_ADDRESS1_INPUT = (By.ID, "address1")
    YA_ADDRESS2_INPUT = (By.ID, "address2")
    YA_CITY_INPUT = (By.ID, "city")
    YA_STATE_SELECT = (By.ID, "id_state")
    YA_POSTCODE_INPUT = (By.ID, "postcode")
    YA_PHONE_MOBILE_INPUT = (By.ID, "phone_mobile")

    SUBMIT_BUTTON = (By.ID, "submitAccount")


class CreateAccountPage:

    def __init__(self, browser):
        self.bp = BasePage(browser)

    def select_mr_radio_button(self):
        self.bp.click(*Locators.YPI_MR_RADIO_BUTTON.value)

    def select_mrs_radio_button(self):
        self.bp.click(*Locators.YPI_MRS_RADIO_BUTTON.value)

    def input_ypi_password(self, text):
        self.bp.input_text(*Locators.YPI_PASSWORD_INPUT.value, text)

    def input_ypi_firstname(self, text):
        self.bp.input_text(*Locators.YPI_FIRSTNAME_INPUT.value, text)

    def input_ypi_lastname(self, text):
        self.bp.input_text(*Locators.YPI_LASTNAME_INPUT.value, text)

    def input_ya_firstname(self, text):
        self.bp.input_text(*Locators.YA_FIRSTNAME_INPUT.value, text)

    def input_ya_lastname(self, text):
        self.bp.input_text(*Locators.YA_LASTNAME_INPUT.value, text)

    def input_ya_address1(self, text):
        self.bp.input_text(*Locators.YA_ADDRESS1_INPUT.value, text)

    def input_ya_city(self, text):
        self.bp.input_text(*Locators.YA_CITY_INPUT.value, text)

    def select_state(self, value):
        self.bp.select_option_by_value(*Locators.YA_STATE_SELECT.value, value)

    def input_ya_postcode(self, text):
        self.bp.input_text(*Locators.YA_POSTCODE_INPUT.value, text)

    def input_ya_phone_mobile(self, text):
        self.bp.input_text(*Locators.YA_PHONE_MOBILE_INPUT.value, text)

    def click_submit(self):
        self.bp.click(*Locators.SUBMIT_BUTTON.value)
