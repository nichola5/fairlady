from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from database import*
from hamcrest import*

@given(u'text, image and link - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'text, image and link - login using username bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'text, image and link - make new text post with image and link')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.attachment_2).send_keys(os.path.join(project_dir, 'resource/husky.jpg'))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(Keys.RETURN + Keys.RETURN + Keys.RETURN)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["link"])
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(3)

@then(u'text, image and link - go to timeline')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'text, image and link - validating image element')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.photo_element).is_displayed()
    sleep(2)

@then(u'text, image and link - validating text post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_text = text_element[0].text
    assert_that(post_text, contains_string(database.userdata["text_validation"]))
    sleep(2)

@then(u'text, image and link - validating link')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_link = text_element[0].text
    assert_that(post_link, contains_string(database.userdata["link_validation"]))
    sleep(2)

@then(u'text, image and link - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'text, image and link - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'text, image and link - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
