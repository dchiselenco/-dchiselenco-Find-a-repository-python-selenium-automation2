# Created by dchis at 3/30/2024
Feature: Search test

  Scenario: User can search a product
    Given Open Target maiin page
    When Search for "coffee"
    Then Verify search results are shown