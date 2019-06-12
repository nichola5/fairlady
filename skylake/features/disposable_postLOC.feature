Feature: post with location
Scenario: post with location
      Given Post location - opening sebangsa
      When  Post location - login using bot_one
      Then  Post location - make new post with location
      Then  Post location - go to timeline
      Then  Post location - validating text post
      Then  Post location - validating location element is displayed
      Then  Post location - validating location as central park
      Then  Post location - deleting post
      When  Post location - logout
      Then  Post location - direct to landing page
