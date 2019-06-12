Feature: post with sticker
Scenario: post with sticker
      Given sticker scenario - opening sebangsa
      When  sticker scenario - login using bot_one
      Then  sticker scenario - make new text post with sticker
      Then  sticker scenario - go to timeline
      Then  sticker scenario - validating text
      Then  sticker scenario - validating sticker element
      Then  sticker scenario - validating sticker type
      Then  sticker scenario - deleting post
      When  sticker scenario - logout
      Then  sticker scenario - direct to sebangsa landing page
