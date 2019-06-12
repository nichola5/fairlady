Feature: vote down scenario
Scenario: vote down scenario
      Given vote down scenario - opening sebangsa
      When  vote down scenario - login as bot_3
      Then  vote down scenario - go to timeline and wait
      Then  vote down scenario - vote down post as user
      Then  vote down scenario - validating vote down as user
      Then  vote down scenario - unvote post
      Then  vote down scenario - validating unvote post and back to default
      When  vote down scenario - logout
      Then  vote down scenario - direct to landing page
