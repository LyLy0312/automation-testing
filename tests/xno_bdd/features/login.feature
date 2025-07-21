Feature: Login to XNO

  Scenario: Log into XNO successfully
    Given the user is on the login page
    When the user logs in with valid credentials
    Then the user should be redirected to the dashboard
