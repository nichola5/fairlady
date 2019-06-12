from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'post quote scenario - opening sebangsa homepage')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'post quote scenario - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'post quote scenario - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'post quote scenario - quote post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.reshare)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.reshare).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.quote).click()
    sleep(3)

@then(u'post quote scenario - write text and send')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.quote_editor).send_keys(database.userdata["text2"])
    sleep(3)
    context.browser.find_element(By.XPATH,locator.quote_exec).click()
    sleep(7)

@then(u'post quote scenario - validating quote element is present')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.quote_card).is_displayed()
    sleep(1)

@then(u'post quote scenario - validating quote post text')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text).is_displayed()
    text_element = context.browser.find_elements(By.XPATH,locator.post_text)
    quote_text = text_element[0].text
    assert_that(quote_text, equal_to_ignoring_whitespace(database.userdata["text2_validation"]))
    sleep(1)

@then(u'post quote scenario - delete quote post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.quote_postmenu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.quote_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_popquote)
    context.browser.find_element(By.XPATH,locator.editor_yesbtnquote).click()
    sleep(5)

@when(u'post quote scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'post quote scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
