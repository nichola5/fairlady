from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'Post location - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'Post location - login using bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'Post location - make new post with location')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(4)
    context.browser.find_element(By.XPATH,locator.editor_base).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_base).send_keys(database.userdata["text"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_baseloc).click()
    context.browser.find_element(By.XPATH,locator.loc_list).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.loc_list).send_keys(database.userdata["location"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.loc3_chosen).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.editor_base_exec).click()
    sleep(5)

@then(u'Post location - go to timeline')
def step_impl(context):

    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'Post location - validating text post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(1)

@then(u'Post location - validating location element is displayed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.loc_element).is_displayed()
    sleep(2)

@then(u'Post location - validating location as central park')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.loc_placename).is_displayed()
    loc_place = context.browser.find_elements(By.XPATH,locator.loc_placename)
    loc_text = loc_place[0].text
    assert_that(loc_text, equal_to_ignoring_case(database.userdata["location_validation"]))
    sleep(1)

@then(u'Post location - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'Post location - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'Post location - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
