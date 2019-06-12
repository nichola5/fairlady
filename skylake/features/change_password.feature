Feature: change password
Scenario: change password
      Given password scenario - opening sebangsa
      When  password scenario - login as bot_two
      Then  password scenario - go to setting
      Then  password scenario - go to password and change password
      Then  password scenario - saving new password
      When  password scenario - logout
      Then  password scenario - direct to sebangsa landing page
      When  password scenario - relogin with new password
      Then  password scenario - back to user setting
      Then  password scenario - go to password again
      Then  password scenario - change to default password
      When  password scenario - logout again
      Then  password scenario - back to landing page
