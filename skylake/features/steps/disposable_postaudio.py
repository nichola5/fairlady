from behave import*
from locator import*
from selenium import webdriver
from database import*
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from hamcrest import*

@given(u'text audio scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'text audio scenario - login using username bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'text audio scenario - make new text post with audio')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.attachment_2).send_keys(os.path.join(project_dir, 'resource/example.m4a'))
    sleep(3)
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(10)

@then(u'text audio scenario - go to timeline')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(8)

@then(u'text audio scenario - validating text post passed')
def step_impl(context):
    #context.browser.find_element(By.XPATH,locator.post_text_x).is_displayed()
    #text_element = context.browser.find_element(By.XPATH,locator.post_text_x)
    #post_text = text_element.text
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(1)

@then(u'text audio scenario - validating audio element and duration passed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.audio_element).is_displayed()
    duration = context.browser.find_elements(By.XPATH,locator.audio_duration)
    duration_text = duration[0].text
    assert_that(duration_text, equal_to(database.userdata["audio_validation"]))
    sleep(1)

@then(u'text audio scenario - deleting post')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'text audio scenario - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'text audio scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
