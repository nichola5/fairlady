Feature: post reshare scenario
Scenario: post reshare scenario
      Given post reshare scenario - opening sebangsa homepage
      When  post reshare scenario - login as bot_3
      Then  post reshare scenario - go to timeline and wait
      Then  post reshare scenario - reshare post
      Then  post reshare scenario - validating reshare element is displayed
      Then  post reshare scenario - cancel reshare post
      When  post reshare scenario - logout
      Then  post reshare scenario - direct to landing page
