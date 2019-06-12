Feature: quickpass community scenario
Scenario: quickpass community scenario
      Given quickpass community scenario - opening sebangsa
      When  quickpass community scenario - login as bot_2
      Then  quickpass community scenario - go to quickpass option
      Then  quickpass community scenario - insert passkey, password and join community
      Then  quickpass community scenario - validating joined
      Then  quickpass community scenario - click joined button to leave
      Then  quickpass community scenario - validating leave community
      Then  quickpass community scenario - logout
      Then  quickpass community scenario - direct to landing page
