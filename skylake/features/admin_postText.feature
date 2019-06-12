Feature: admin text Post
Scenario: admin text Post
      Given admin text post - opening sebangsa
      When  admin text post - login using bot_one as admin
      Then  admin text post - go to community
      Then  admin text post - make a new text post as admin
      Then  admin text post - validating text post passed
      Then  admin text post - deleting post
      When  admin text post - user logout
      Then  admin text post - direct to landing page
