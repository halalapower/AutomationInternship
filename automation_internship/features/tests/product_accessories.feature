# Created by labzizihind at 2/15/22
Feature: Test scenario for accessories


  Scenario: User can see all items under ACCESSORIES

    Given Open GetTop page
    When Hover over accessories
    Then Verify 3 items are shown under accessories

  Scenario: User can open each of the products under ACCESSORIES category

    Given Open GetTop page
    When Hover over accessories
    Then Click_and_verify_product
