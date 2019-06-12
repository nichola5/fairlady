Feature: create new community
Scenario: create new community
      Given create comm scenario - opening sebangsa
      When  create comm scenario - login as bot_one
      Then  create comm scenario - create test_legion1 community
      Then  create comm scenario - add bio in description
      Then  create comm scenario - go to setting and set avatar
      Then  create comm scenario - back to profile
      Then  create comm scenario - go to setting and delete test_legion1
      When  create comm scenario - logout as bot_one
      Then  create comm scenario - direct to landing page
