Feature: Disposable text Post
Scenario: Disposable text Post
      Given text post - opening sebangsa
      When  text post - login using username bot_one
      Then  text post - make new text post
      Then  text post - go to timeline
      Then  text post - validating text post passed
      Then  text post - deleting post
      When  text post - user logout
      Then  text post - direct to landing page
