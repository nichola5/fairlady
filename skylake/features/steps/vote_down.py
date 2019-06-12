from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'vote down scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'vote down scenario - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'vote down scenario - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'vote down scenario - vote down post as user')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_down).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.vote_down_usr).click()
    sleep(3)

@then(u'vote down scenario - validating vote down as user')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote2_component).is_displayed()
    vd_element = context.browser.find_elements(By.XPATH,locator.vote2_component)
    vd_usr = vd_element[0].get_attribute("title")
    #print(vd_usr)
    assert_that(vd_usr, equal_to(database.userdata["vote_down_usr"]))
    sleep(1)

@then(u'vote down scenario - unvote post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_down).click()
    sleep(3)

@then(u'vote down scenario - validating unvote post and back to default')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_down).is_displayed()
    vote_down = context.browser.find_element(By.XPATH,locator.vote_down).text
    assert_that(vote_down, equal_to(database.userdata["vote_down_before"]))
    sleep(2)

@when(u'vote down scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'vote down scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
