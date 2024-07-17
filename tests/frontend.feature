@frontend
Feature: Frontend tests
    Scenario: Listing of devices on data page
        Given that devices exist
        When I navigate to the data page
        Then all devices should be listed

    Scenario Outline: Navigating to pages
        Given that I am on the homepage
        When I press the <site> navbar button 
        Then I should be on the <path> site

        Examples:
            | site   | path   |
            | Home   | home   |
            | Data   | data   |
            | Camera | camera |