Feature: Different computations on QuarticSDK

  Scenario: test different internal method flows in sdk
    Given we have successfully set up client and mocked requests method
    When we call different internal methods
    Then the return matches the expectations
