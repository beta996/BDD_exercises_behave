# Created by bjackowska3 at 12/3/2022
Feature: checking if the url is the same as the one inputted


  # Test to check whether selenium driver returns a correct url
  Scenario: The selenium home page should have correct url
    Given I go to https://www.selenium.dev
    Then current url should be https://www.selenium.dev/

    # Test to check whether selenium driver returns a correct url
  Scenario: The selenium page should have a 'main navbar' div and it should be visible
    Given I go to https://www.selenium.dev
    Then main navigation bar should be existing
    And main navigation bar should be visible


  Scenario Outline: my test
    Given I go to <website>
    Then  current url should be <expected_url>
    Examples:
      | website | expected_url
      | https://www.selenium.dev | https://www.selenium.dev/
      | https://www.selenium.dev | https://www.selenium.dev/
