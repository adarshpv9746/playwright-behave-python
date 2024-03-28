Feature: As a user,  i want to be able to log in page

  Scenario: Given a user, i can access login page
    Given the application is loaded
    When i see the application page
    Then the login page should be displayed