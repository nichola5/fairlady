Feature: set and unset admin scenario
Scenario: set and unset admin scenario
      Given set and unset admin scenario - opening sebangsa
      When  set and unset admin scenario - login as community owner
      Then  set and unset admin scenario - go to community tab and find community
      When  set and unset admin scenario - go to member page and set member as admin
      Then  set and unset admin scenario - log out as owner and login as member
      Then  set and unset admin scenario - accept request as admin
      Then  set and unset admin scenario - logout as member and login as owner
      Then  set and unset admin scenario - validating admin label and unset member as admin
      Then  set and unset admin scenario - logout
      Then  set and unset admin scenario - direct to landing page
