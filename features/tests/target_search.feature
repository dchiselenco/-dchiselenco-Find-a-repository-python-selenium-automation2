# Created by dchis at 3/30/2024
Feature: Search tests

  Scenario: User can search for a coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: User can search for tea
    Given Open Target main page
    When Search for tea
    Then Verify search results are shown for tea

  Scenario Outline: User can search for an item
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_product>
    Examples:
    |item     |expected_product   |
    |mug      |mug                |
    |tea      |tea                |
    |coffee   |coffee             |
