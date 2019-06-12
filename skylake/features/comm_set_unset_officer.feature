Feature: set and unset officer scenario
Scenario: set and unset officer scenario
      Given set and unset officer scenario - opening sebangsa
      When  set and unset officer scenario - login as community owner
      Then  set and unset officer scenario - go to community tab and find community
      When  set and unset officer scenario - go to member page and set member as officer
      Then  set and unset officer scenario - create label for officer
      Then  set and unset officer scenario - validating member as officer
      Then  set and unset officer scenario - unset member as officer
      Then  set and unset officer scenario - logout
      Then  set and unset officer scenario - direct to landing page
