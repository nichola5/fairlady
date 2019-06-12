from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'edit scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'edit scenario - login using bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'edit scenario - make new - this is a bot test 01- post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    sleep(1)

@then(u'edit scenario - send post and go to timeline')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'edit scenario - go to post setting and edit post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_edit).click()
    sleep(1)

@then(u'edit scenario - delete existing text')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_container2).send_keys(Keys.CONTROL + "a")
    context.browser.find_element(By.XPATH,locator.editor_container2).send_keys(Keys.DELETE)

@then(u'edit scenario - write new text to -post override- and send')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_container2).send_keys(database.userdata["text2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_edit_exec).click()


@then(u'edit scenario - back to timeline')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(5)

@then(u'edit scenario - validating new text as -post override-')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    edit_text = text_element[0].text
    assert_that(edit_text, contains_string(database.userdata["text2_validation"]))
    sleep(1)

@then(u'edit scenario - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'edit scenario - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'edit scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
