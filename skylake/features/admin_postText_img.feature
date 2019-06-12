Feature: admin text IMG Post
Scenario: admin text IMG Post
      Given admin text IMG Post - opening sebangsa
      When  admin text IMG Post - login using bot_one as admin
      Then  admin text IMG Post - go to community
      Then  admin text IMG Post - make a new text post with images as admin
      Then  admin text IMG Post - validating text post passed
      Then  admin text IMG Post - validating images passed
      Then  admin text IMG Post - deleting post
      When  admin text IMG Post - user logout
      Then  admin text IMG Post - direct to landing page
