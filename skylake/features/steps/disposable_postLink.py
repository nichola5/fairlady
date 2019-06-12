from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from database import*
from time import sleep
from hamcrest import*

@given(u'link scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'link scenario - login using bot_one')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'link scenario - make new post with link')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(Keys.RETURN + Keys.RETURN + Keys.RETURN)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["link"])
    context.browser.find_element(By.XPATH,locator.editor_execution).click()


@then(u'link scenario - go to timeline')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'link scenario - validating text post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.post_text2).is_displayed()
    text_element = context.browser.find_element(By.XPATH,locator.post_text2)
    post_text = text_element.text
    assert_that(post_text, contains_string(database.userdata["text_validation"]))
    sleep(1)

@then(u'link scenario - validating link')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.link_text).is_displayed()
    link_url = context.browser.find_element(By.XPATH,locator.link_text)
    link = link_url.text
    assert_that(link, contains_string(database.userdata["link_validation"]))
    sleep(1)

@then(u'link scenario - validating link element')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.link_element).is_displayed()
    sleep(1)


@then(u'link scenario - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)


@when(u'link scenario - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'link scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
