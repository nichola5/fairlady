from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'join and leave community scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'join and leave community scenario - login as bot_2')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'join and leave community scenario - go to search bar and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.search).click()
    context.browser.find_element(By.XPATH,locator.search).send_keys(database.userdata["north_community"])
    context.browser.find_element(By.XPATH,locator.search).send_keys(Keys.ENTER)
    sleep(10)

@when(u'join and leave community scenario - in the community profile, click join button')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_north).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).click()
    sleep(1)


@then(u'join and leave community scenario - insert password and join community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_popup).is_displayed()
    context.browser.find_element(By.XPATH,locator.comm_join_pass).click()
    context.browser.find_element(By.XPATH,locator.comm_join_pass).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.comm_join_exec).click()
    sleep(5)


@then(u'join and leave community scenario - validating joined')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).is_displayed()
    joined = context.browser.find_element(By.XPATH,locator.comm_joinbtn).text
    assert_that(joined, contains_string("Joined"))
    sleep(3)

@then(u'join and leave community scenario - click joined button to leave')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_leave_pop).is_displayed()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_leave_exec).click()
    sleep(5)

@then(u'join and leave community scenario - validating leave community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).is_displayed()
    join = context.browser.find_element(By.XPATH,locator.comm_joinbtn).text
    assert_that(join, contains_string("Join"))
    sleep(3)

@then(u'join and leave community scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'join and leave community scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
