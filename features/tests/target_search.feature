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
    Then Verify that URL has tea

  Scenario Outline: User can search for an item
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_product>
    Examples:
    |item      |expected_product   |
    |mug       |mug                |
    |tea       |tea                |
    |coffee    |coffee             |
    |white mug |white mug          |


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image


  Scenario: User can see favorites tootlip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown