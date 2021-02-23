Feature: Following feature refers to all the possible steps performed by the user

  Scenario: test that the methods present in the sdk are working correctly
    Given we have successfully setup the client to test the methods
    When we call all the different possible methods in the entities
    Then the methods works correctly resulting in correct data types
