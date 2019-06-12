from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'vote up scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'vote up scenario - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'vote up scenario - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'vote up scenario - vote up post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_up).click()
    sleep(3)

@then(u'vote up scenario - validating vote up post active')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_component).is_displayed()
    vote_stat = context.browser.find_element(By.XPATH,locator.vote_stat).text
    assert_that(vote_stat, equal_to(database.userdata["vote_up_after"]))
    sleep(2)

@then(u'vote up scenario - unvote post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_up).click()
    sleep(3)

@then(u'vote up scenario - validating vote up post back to default')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_up).is_displayed()
    vote_active = context.browser.find_element(By.XPATH,locator.vote_stat).text
    assert_that(vote_active, equal_to(database.userdata["vote_up_before"]))
    sleep(2)

@when(u'vote up scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'vote up scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
