Feature: post link with image
Scenario: post link with image
      Given text, image and link - opening sebangsa
      When  text, image and link - login using username bot_one
      Then  text, image and link - make new text post with image and link
      Then  text, image and link - go to timeline
      Then  text, image and link - validating image element
      Then  text, image and link - validating text post
      Then  text, image and link - validating link
      Then  text, image and link - deleting post
      When  text, image and link - logout
      Then  text, image and link - direct to landing page
