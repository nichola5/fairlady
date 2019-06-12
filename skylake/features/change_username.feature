Feature: change user name
Scenario: change user name
      Given change name scenario - opening sebangsa
      When  change name scenario - login using bot_two
      Then  change name scenario - go to user setting
      Then  change name scenario - delete existing name and change full name
      Then  change name scenario - save profile and back to timeline
      When  change name scenario - open setting and logout
      Then  change name scenario - direct to landing page
