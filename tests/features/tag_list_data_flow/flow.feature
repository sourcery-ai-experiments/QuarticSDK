Feature: Fetch tag list data with and without transformations

  Scenario: test tags data flow in the SDK
    Given we have successfully set up client to test tags data flow
    When we call the required methods to get the tags list data
    Then the return of tag list data works correctly for json and pandas df
