Feature: post quote scenario
Scenario: post quote scenario
      Given post quote scenario - opening sebangsa homepage
      When  post quote scenario - login as bot_3
      Then  post quote scenario - go to timeline and wait
      Then  post quote scenario - quote post
      Then  post quote scenario - write text and send
      Then  post quote scenario - validating quote element is present
      Then  post quote scenario - validating quote post text
      Then  post quote scenario - delete quote post
      When  post quote scenario - logout
      Then  post quote scenario - direct to landing page
