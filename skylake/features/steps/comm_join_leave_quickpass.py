from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*
import os

#dev = export BASE_URL=https://gatotkaca.jog.ojodowo.com/ && a=A && b=E && c=1 && d=8 && e=2
#live = export BASE_URL=http://sebangsa.com/ && a=A && b=E && c=3 && d=4 && e=5

@given(u'quickpass community scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'quickpass community scenario - login as bot_2')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'quickpass community scenario - go to quickpass option')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.quickpass).click()
    sleep(2)

@then(u'quickpass community scenario - insert passkey, password and join community')
def step_impl(context):
    
    a = os.environ["a"]
    context.browser.find_element(By.XPATH,locator.qck_pass1).send_keys(a)
    sleep(1)
    b = os.environ["b"]
    context.browser.find_element(By.XPATH,locator.qck_pass2).send_keys(b)
    sleep(1)
    c = os.environ["c"]
    context.browser.find_element(By.XPATH,locator.qck_pass3).send_keys(c)
    sleep(1)
    d = os.environ["d"]
    context.browser.find_element(By.XPATH,locator.qck_pass4).send_keys(d)
    sleep(1)
    e = os.environ["e"]
    context.browser.find_element(By.XPATH,locator.qck_pass5).send_keys(e)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_join_pass).click()
    context.browser.find_element(By.XPATH,locator.comm_join_pass).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.comm_join_exec).click()
    sleep(5)


@then(u'quickpass community scenario - validating joined')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).is_displayed()
    joined = context.browser.find_element(By.XPATH,locator.comm_joinbtn).text
    assert_that(joined, contains_string("Joined"))
    sleep(3)

@then(u'quickpass community scenario - click joined button to leave')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_leave_pop).is_displayed()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_leave_exec).click()
    sleep(5)

@then(u'quickpass community scenario - validating leave community')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_joinbtn).is_displayed()
    join = context.browser.find_element(By.XPATH,locator.comm_joinbtn).text
    assert_that(join, contains_string("Join"))
    sleep(3)

@then(u'quickpass community scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'quickpass community scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
