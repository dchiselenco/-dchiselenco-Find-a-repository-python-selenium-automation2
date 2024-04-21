# Created by dchis at 4/17/2024
Feature:Target Circle page
  #  Create a test case that will open the Target Circle page
  #  https://www.target.com/circle, and verify there are 10 benefit cells

  Scenario: Verify there are correct amount benefit cells on the page
    Given Open the Target Circle page
    Then 10 benefit cells are shown
