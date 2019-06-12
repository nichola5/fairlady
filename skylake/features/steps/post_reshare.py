from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'post reshare scenario - opening sebangsa homepage')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'post reshare scenario - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'post reshare scenario - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'post reshare scenario - reshare post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.reshare).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.reshare_exec).click()
    sleep(5)

@then(u'post reshare scenario - validating reshare element is displayed')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.reshare_element).is_displayed()
    sleep(3)

@then(u'post reshare scenario - cancel reshare post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.reshare).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.reshare_cancel).click()
    sleep(5)

@when(u'post reshare scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'post reshare scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
