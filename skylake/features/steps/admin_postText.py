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


@given(u'admin text post - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'admin text post - login using bot_one as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username6"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'admin text post - go to community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(2)


@then(u'admin text post - make a new text post as admin')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_editor)
    context.browser.find_element(By.XPATH,locator.comm_editor).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.comm_editorexec).click()
    sleep(6)

@then(u'admin text post - validating text post passed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.comm_text)
    post_text = text_element[0].text
    assert_that(post_text, equal_to_ignoring_whitespace(database.userdata["text_validation"]))
    sleep(1)


@then(u'admin text post - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_name).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN)
    sleep(3)
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


@when(u'admin text post - user logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'admin text post - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
