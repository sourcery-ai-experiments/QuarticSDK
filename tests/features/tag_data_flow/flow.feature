Feature: Computations to fetch tag data from the sdk

  Scenario: test tag data flow in the SDK
    Given we have successfully set up client to test tag data flow
    When we call the required methods to get the tag details
    Then the return of tag data works correctly for json and pandas df
