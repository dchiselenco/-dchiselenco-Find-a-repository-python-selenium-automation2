# Created by dchis at 4/1/2024
Feature: Cart test

  Scenario: Verify message “Your cart is empty”
    Given Open Target main page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown

  Scenario: Verify the added item is in cart
    Given Open Target main page
    When Search for tea
    Then Select an item
    Then Add item to cart
    Then Cart message for added item
