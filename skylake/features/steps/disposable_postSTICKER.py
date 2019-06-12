from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'sticker scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'sticker scenario - login using bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'sticker scenario - make new text post with sticker')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.editor_stckr_main).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_stckr_sub).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_stckr1).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(5)

@then(u'sticker scenario - go to timeline')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'sticker scenario - validating text')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(1)

@then(u'sticker scenario - validating sticker element')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.stc_element).is_displayed()
    sleep(2)

@then(u'sticker scenario - validating sticker type')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.stc_element).is_displayed()
    stc_element = context.browser.find_elements(By.XPATH,locator.card_content)
    #print(dir(stc_element[0]))
    stc_val = stc_element[0].find_element_by_tag_name("img").get_attribute("src")
    #print(stc_val)
    #print(dir(stc_val))
    assert_that(stc_val, contains_string(database.userdata["sticker_validation"]))
    sleep(1)

@then(u'sticker scenario - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'sticker scenario - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'sticker scenario - direct to sebangsa landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
