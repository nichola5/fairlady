Feature: edit post scenario
Scenario: edit post scenario
      Given edit scenario - opening sebangsa
      When  edit scenario - login using bot_one
      Then  edit scenario - make new - this is a bot test 01- post
      Then  edit scenario - send post and go to timeline
      Then  edit scenario - go to post setting and edit post
      Then  edit scenario - delete existing text
      Then  edit scenario - write new text to -post override- and send
      Then  edit scenario - back to timeline
      Then  edit scenario - validating new text as -post override-
      Then  edit scenario - deleting post
      When  edit scenario - logout
      Then  edit scenario - direct to landing page
