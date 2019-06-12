Feature: owner text audio Post
Scenario: owner text audio Post
      Given owner text audio Post - opening sebangsa
      When  owner text audio Post - login using bot_one as owner
      Then  owner text audio Post - go to community
      Then  owner text audio Post - make a new text post with audio as owner
      Then  owner text audio Post - validating text post passed
      Then  owner text audio Post - validating audio passed
      Then  owner text audio Post - deleting post
      When  owner text audio Post - user logout
      Then  owner text audio Post - direct to landing page
