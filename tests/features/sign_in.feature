Feature: Sign In


  Background:
    Given the app is displayed

  Scenario: Success create account
    When I go to sign in page
    When I create account
    When I import correct data in form
    When I submit create account form
    Then some check