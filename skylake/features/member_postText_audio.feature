Feature: member text audio Post
Scenario: member text audio Post
      Given member text audio Post - opening sebangsa
      When  member text audio Post - login using bot_one as member
      Then  member text audio Post - go to community
      Then  member text audio Post - make a new text post with audio as member
      Then  member text audio Post - validating text post passed
      Then  member text audio Post - validating audio passed
      Then  member text audio Post - deleting post
      When  member text audio Post - user logout
      Then  member text audio Post - direct to landing page
