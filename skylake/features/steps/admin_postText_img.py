from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
import os
from pathlib import Path
from hamcrest import*


@given(u'admin text IMG Post - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'admin text IMG Post - login using bot_one as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username6"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'admin text IMG Post - go to community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(2)


@then(u'admin text IMG Post - make a new text post with images as admin')
def step_impl(context):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_editor)
    context.browser.find_element(By.XPATH,locator.comm_editor).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.comm_attch).send_keys(os.path.join(project_dir, 'resource/husky.jpg'))
    context.browser.find_element(By.XPATH,locator.comm_attch2).send_keys(os.path.join(project_dir, 'resource/theodore.jpg'))
    context.browser.find_element(By.XPATH,locator.comm_attch2).send_keys(os.path.join(project_dir, 'resource/aerith.jpg'))
    context.browser.find_element(By.XPATH,locator.comm_attch2).send_keys(os.path.join(project_dir, 'resource/upin_ipin.jpg'))
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_editorexec).click()
    sleep(10)

@then(u'admin text IMG Post - validating text post passed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_name)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.comm_name).click()
    sleep(8)
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN + Keys.PAGE_DOWN)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.comm_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(5)


@then(u'admin text IMG Post - validating images passed')
def step_impl(context):
    photo = context.browser.find_elements(By.XPATH,locator.photosets)
    sets = photo[0].find_elements(By.CLASS_NAME, "photoset__item")
    sleep(1)
    assert_that(sets, has_length(equal_to(4)))
    sleep(3)


@then(u'admin text IMG Post - deleting post')
def step_impl(context):

    context.browser.find_element(By.XPATH,locator.comm_editor_option).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_editor_option).send_keys(Keys.PAGE_DOWN)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_post_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)
    #context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'admin text IMG Post - user logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'admin text IMG Post - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
