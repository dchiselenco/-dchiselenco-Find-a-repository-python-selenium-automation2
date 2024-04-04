# Created by dchis at 4/1/2024
Feature: sign in form

  Scenario: Verify Sign In form opened
    Given Open target.com
    When Click Sign In
    When From right side navigation menu click Sign In
    Then Verify Sign In form opened