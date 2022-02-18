# Created by labzizihind at 2/16/22
Feature: Test cases for Top banner tickets
  # Enter feature description here

  Scenario: User can click right and left arrows to see top banners
    Given Open GetTop page
    When Hover over top banner
    Then Click the right arrow icon
    Then Store next page product name
    Then Click the left arrow icon
    Then store first page product name
    Then verify different products are available

  Scenario: User can click bottom dots to see top banners
    Given Open GetTop page
    When Hover over top banner
    Then Click the bottom right dot
    Then Store next page product name
    Then Click the bottom left dot
    Then store first page product name
    Then verify different products are available


#  Scenario: User can click on product banner and is taken to correct category page
#    Given Open GetTop page
#    Then Click through top banner links
#    Then Verify correct pages are open