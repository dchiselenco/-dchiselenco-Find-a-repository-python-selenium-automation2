# Created by dchis at 4/21/2024
Feature: Tests for main page UI
  # Enter feature description here

  Scenario: Verify header is shown
    Given Open Target main page
    Then Verify header is shown


  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 5 links