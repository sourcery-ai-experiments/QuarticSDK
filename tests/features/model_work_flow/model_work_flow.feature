Feature: Creating And Saving a model to Quartic Platform
  Scenario: Test if Creating and Saving model fails if Prediction returns non numerics Fails
    Given A Model wrapped in BaseQuarticModel and returns predictions output as string
    And  A Quartic SDK APIClient
    When Model save is called with proper parameters
    Then Raises a InvalidPredictionException

  Scenario: Test if Creating and Saving model fails if prediction returns results slower than configured
    Given A Model wrapped in BaseQuarticModel and sleeps for n seconds before returning the results
    And  A Quartic SDK APIClient
    When Model save is called with proper parameters
    Then Raises a InvalidPredictionException

  Scenario: Test if Creating and Saving model fails if prediction returns non pandas series
    Given A Model wrapped in BaseQuarticModel and returns prediction output as list
    And  A Quartic SDK APIClient
    When Model save is called with proper parameters
    Then Raises a InvalidPredictionException

  Scenario: Test if Creating and Saving model fails if prediction returns all nulls
    Given A Model wrapped in BaseQuarticModel and returns prediction output as all Null
    And  A Quartic SDK APIClient
    When Model save is called with proper parameters
    Then Raises a InvalidPredictionException

  Scenario: Test if Creating and Saving model Succeeds if model is proper
    Given A Model wrapped in BaseQuarticModel and has all proper parameters
    And  A Quartic SDK APIClient
    When Model save is called with proper parameters
    Then Returns a None response without exception

  Scenario: Test if Creating and Saving model maintains user logs
    Given A Model wrapped in BaseQuarticModel with a mock log handler added
    When Model predict is called with logging
    Then adds user logs to handler
