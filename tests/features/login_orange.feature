Feature: To test login functionality with valid and invalid credentials

  Scenario: Test the login with a Valid credentials
    Given url as "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    And username as "Admin" and password as "admin123"
    When user clicks on login button
    Then the text "Dashboard" should be displayed
    And logout from the application


 Scenario Outline: Test the login with a Invalid credentials
    Given url as "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    And username as "<username>" and password as "<password>"
    When user clicks on login button
    #Then the text "Dashboard" should be displayed
   Examples:
     |username  |password|
     |abc       |123    |
     |xyz       |456    |

