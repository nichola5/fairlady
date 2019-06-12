Feature: vote up scenario b
Scenario: vote up scenario b
      Given vote up scenario b - opening sebangsa
      When  vote up scenario b - login as bot_3
      Then  vote up scenario b - go to timeline and wait
      Then  vote up scenario b - vote up post
      Then  vote up scenario b - validating vote up post active
      Then  vote up scenario b - unvote post
      Then  vote up scenario b - validating vote up post back to default
      When  vote up scenario b - logout
      Then  vote up scenario b - direct to landing page
