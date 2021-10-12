@one
Feature: drag and drop

  Scenario: dropped succesffully
    Given The user navigate to the drag and drop URL
    When he move the drag box to drop box
    Then he see the message change to Dropped!