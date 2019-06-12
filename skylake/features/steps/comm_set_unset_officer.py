from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'set and unset officer scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'set and unset officer scenario - login as community owner')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'set and unset officer scenario - go to community tab and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(4)

@when(u'set and unset officer scenario - go to member page and set member as officer')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_member).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member).send_keys(Keys.PAGE_DOWN)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_set_officer).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.popup).is_displayed()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_officer_exec).click()
    sleep(5)


@then(u'set and unset officer scenario - create label for officer')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_officer_labelinput).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_officer_labelinput).send_keys(database.userdata["officer"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_officer_labexec).click()
    sleep(5)

@then(u'set and unset officer scenario - validating member as officer')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_member).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member).send_keys(Keys.PAGE_DOWN)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_officer_validate).is_displayed()
    officer = context.browser.find_element(By.XPATH,locator.comm_label_validation)
    label = officer.text
    assert_that(label, contains_string(database.userdata["officer_validation"]))
    sleep(1)

@then(u'set and unset officer scenario - unset member as officer')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_member_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_officer_unset).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.popup).is_displayed()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_officer_unsetexec).click()
    sleep(5)


@then(u'set and unset officer scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'set and unset officer scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
