Feature: join and leave community scenario
Scenario: join and leave community scenario
      Given join and leave community scenario - opening sebangsa
      When  join and leave community scenario - login as bot_2
      Then  join and leave community scenario - go to search bar and find community
      When  join and leave community scenario - in the community profile, click join button
      Then  join and leave community scenario - insert password and join community
      Then  join and leave community scenario - validating joined
      Then  join and leave community scenario - click joined button to leave
      Then  join and leave community scenario - validating leave community
      Then  join and leave community scenario - logout
      Then  join and leave community scenario - direct to landing page
