from datetime import datetime
import time

from pytest_bdd import scenario, when, then, parsers

from pages.create_account_page import CreateAccountPage
from pages.header import Header
from pages.sign_in_page import SignInPage


@scenario('../features/sign_in.feature', 'Success create account')
def test_sign_in():
    pass


@when("I go to sign in page")
def go_to_sign_in_page(browser):
    header = Header(browser)
    header.click_sign_in()


@when("I create account")
def go_to_sign_in_page(browser):
    sip = SignInPage(browser)
    sip.input_email_create('a' + str(int(round(time.time()))) + '@m.com')
    sip.click_create_button()
    time.sleep(5)


@when("I import correct data in form")
def success_fill_form(browser):
    cap = CreateAccountPage(browser)

    cap.input_ypi_firstname("aaaaa")
    cap.input_ypi_lastname("aaaaa")
    cap.input_ypi_lastname("aaaaa")
    cap.input_ypi_password("aaaaa")

    cap.input_ya_address1("ffffjddlkdksj")
    cap.input_ya_city("Alabama")
    cap.select_state('1')
    cap.input_ya_postcode("12345")
    cap.input_ya_phone_mobile("1234567")


@when("I submit create account form")
def submit_create_account_form(browser):
    cap = CreateAccountPage(browser)
    cap.click_submit()
    time.sleep(5)


@then("some check")
def some_check(browser):
    header = Header(browser)
    assert header.get_account_name() == 'aaaaa aaaaaaaaaa'
    time.sleep(5)
    pass
