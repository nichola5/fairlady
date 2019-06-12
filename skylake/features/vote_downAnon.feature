Feature: vote down anonymous scenario
Scenario: vote down anonymous scenario
      Given vote down anonymous scenario - opening sebangsa
      When  vote down anonymous scenario - login as bot_3
      Then  vote down anonymous scenario - go to timeline and wait
      Then  vote down anonymous scenario - vote down post as anonymous
      Then  vote down anonymous scenario - validating vote down as anonymous
      Then  vote down anonymous scenario - unvote post
      Then  vote down anonymous scenario - validating unvote post and back to default
      When  vote down anonymous scenario - logout
      Then  vote down anonymous scenario - direct to landing page
