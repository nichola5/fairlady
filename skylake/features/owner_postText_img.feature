Feature: owner text IMG Post
Scenario: owner text IMG Post
      Given owner text IMG Post - opening sebangsa
      When  owner text IMG Post - login using bot_one as owner
      Then  owner text IMG Post - go to community
      Then  owner text IMG Post - make a new text post with images as owner
      Then  owner text IMG Post - validating text post passed
      Then  owner text IMG Post - validating images passed
      Then  owner text IMG Post - deleting post
      When  owner text IMG Post - user logout
      Then  owner text IMG Post - direct to landing page
