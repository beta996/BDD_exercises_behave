# Created by bjackowska3 at 12/12/2022
Feature: My account test
  # Enter feature description here

  Scenario: Valid user is able to log in
    Given I go to my-account
    When I type beata@beata.com into username form
    And I type Beata1234567* into password form
    And I click login button