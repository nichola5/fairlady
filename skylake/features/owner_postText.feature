Feature: owner text Post
Scenario: owner text Post
      Given owner text post - opening sebangsa
      When  owner text post - login using bot_one as owner
      Then  owner text post - go to community
      Then  owner text post - make a new text post as owner
      Then  owner text post - validating text post passed
      Then  owner text post - deleting post
      When  owner text post - user logout
      Then  owner text post - direct to landing page
