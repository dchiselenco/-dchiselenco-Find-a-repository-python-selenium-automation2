# Created by dchis at 4/1/2024
Feature: verify cart icon

  Scenario: user can see “Your cart is empty” message
    Given Open Target main page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown