Feature: Display login error messages 
   User shoud see correct error message when login fails

  Scenario: Check the error message when login with blank username and password
    Given User should navigate to login page
    When User enters the empty Username and Password
    Then User should see the correct error message

  Scenario: Check the error message when login with blank password
    Given User should navigate to login page
    When User enters Username and no Password
    Then User should see the Password is required error message

  Scenario: Check the user logs in successfully
    Given User should navigate to login page
    When User enters correct Username and Password
    Then Navigate user to shop home page