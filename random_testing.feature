# Created by bjackowska3 at 12/7/2022
Feature: exercise feature
  # Dummy exercises

  Scenario: # check the form validation mechanisms

    Given the user goes to the registration page
    When he put all the details
    And clicks on the submit button
    Then the success message appears

  Scenario: # registering with existing email
    Given the user fills the form with the details and submit
    When it already exists
    Then he should see the error message