Feature: Fetch Data Source Data with and without transformations

  Scenario: test data source data flow in the SDK
    Given we have successfully set up client to test data source data flow
    When we call the required methods to get the data source data
    Then the return of data source data works correctly for json and pandas df
