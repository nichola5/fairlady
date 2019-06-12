Feature: member text Post
Scenario: member text Post
      Given member text post - opening sebangsa
      When  member text post - login using bot_one as member
      Then  member text post - go to community
      Then  member text post - make a new text post as member
      Then  member text post - validating text post passed
      Then  member text post - deleting post
      When  member text post - user logout
      Then  member text post - direct to landing page
