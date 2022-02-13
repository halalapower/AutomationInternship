# Created by YassineNehri at 2/12/22
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a {product} on Get-top website
    Given Open GetTop page
    When Input product into Get-top search
    When Click on Get-top search icon
    Then Verify search worked