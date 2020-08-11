from selenium import webdriver


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, how, what):
        element = self.browser.find_element(how, what)
        element.click()

    def input_text(self, how, what, text):
        element = self.browser.find_element(how, what)
        element.send_keys(text)

    def select_option_by_value(self, how, what, value):
        element = self.browser.find_element(how, what)
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == value:
                option.click()
                break

    def get_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element.text
