# Created by dchis at 4/1/2024
Feature: Sign in form

  Scenario: Verify Sign In form opened
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu click Sign In
    Then Verify Sign In form opened


  Scenario: User can open and close Terms and Conditions from Sign in page
    Given Open Target main page
    When Store original window
    And Click Sign In
    And From right side navigation menu click Sign In
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window
