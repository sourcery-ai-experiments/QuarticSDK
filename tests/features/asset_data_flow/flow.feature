Feature: Computations to fetch asset data from sdk

  Scenario: test asset data flow in the SDK
    Given we have successfully set up client to test asset data flow
    When we call the required methods to get the asset data
    Then the return of asset data works correctly for json and pandas df
