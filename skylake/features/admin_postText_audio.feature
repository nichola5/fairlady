Feature: admin text audio Post
Scenario: admin text audio Post
      Given admin text audio Post - opening sebangsa
      When  admin text audio Post - login using bot_one as admin
      Then  admin text audio Post - go to community
      Then  admin text audio Post - make a new text post with audio as admin
      Then  admin text audio Post - validating text post passed
      Then  admin text audio Post - validating audio passed
      Then  admin text audio Post - deleting post
      When  admin text audio Post - user logout
      Then  admin text audio Post - direct to landing page
