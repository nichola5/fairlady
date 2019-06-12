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


@given(u'text image scenario2 - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'text image scenario2 - login using username bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'text image scenario2 - make new text post with four images')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.attachment_2).send_keys(os.path.join(project_dir, 'resource/husky.jpg'))
    context.browser.find_element(By.XPATH,locator.attachment_2a).send_keys(os.path.join(project_dir, 'resource/theodore.jpg'))
    context.browser.find_element(By.XPATH,locator.attachment_2a).send_keys(os.path.join(project_dir, 'resource/aerith.jpg'))
    context.browser.find_element(By.XPATH,locator.attachment_2a).send_keys(os.path.join(project_dir, 'resource/upin_ipin.jpg'))
    sleep(3)
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(3)

@then(u'text image scenario2 - go to timeline')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'text image scenario2 - validating text')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(1)

@then(u'text image scenario2 - validating photosets element')
def step_impl(context):
    photo = context.browser.find_elements(By.XPATH,locator.photosets)
    sets = photo[0].find_elements(By.CLASS_NAME, "photoset__item")
    sleep(1)
    assert_that(sets, has_length(equal_to(4)))
    sleep(3)

@then(u'text image scenario2 - validating photosets_2 element')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.photosets_2).is_displayed()
    sleep(1)

@then(u'text image scenario2 - validating photosets_3 element')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.photosets_3).is_displayed()
    sleep(1)

@then(u'text image scenario2 - validating photosets_4 element')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.photosets_4).is_displayed()
    sleep(5)

@then(u'text image scenario2 - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(8)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'text image scenario2 - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'text image scenario2 - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
