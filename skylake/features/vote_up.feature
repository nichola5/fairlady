Feature: vote up scenario
Scenario: vote up scenario
      Given vote up scenario - opening sebangsa
      When  vote up scenario - login as bot_3
      Then  vote up scenario - go to timeline and wait
      Then  vote up scenario - vote up post
      Then  vote up scenario - validating vote up post active
      Then  vote up scenario - unvote post
      Then  vote up scenario - validating vote up post back to default
      When  vote up scenario - logout
      Then  vote up scenario - direct to landing page
