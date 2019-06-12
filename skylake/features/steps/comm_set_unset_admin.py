from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'set and unset admin scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'set and unset admin scenario - login as community owner')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'set and unset admin scenario - go to community tab and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(4)

@when(u'set and unset admin scenario - go to member page and set member as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_member).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member).send_keys(Keys.PAGE_DOWN)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_set_admin).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm__admin_popup).is_displayed()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_admin_exec).click()
    sleep(5)


@then(u'set and unset admin scenario - log out as owner and login as member')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(5)

    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username4"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()
    sleep(5)


@then(u'set and unset admin scenario - accept request as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.notification).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.notif_options).is_displayed()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.accept).click()
    sleep(4)

@then(u'set and unset admin scenario - logout as member and login as owner')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(5)

    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()
    sleep(5)

@then(u'set and unset admin scenario - validating admin label and unset member as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_member).send_keys(Keys.PAGE_DOWN)
    sleep(2)

    context.browser.find_element(By.XPATH,locator.comm_officer_validate).is_displayed()
    label = context.browser.find_element(By.XPATH,locator.comm_label_validation)
    admin = label.text
    assert_that(admin, contains_string(database.userdata["admin"]))
    sleep(3)

    context.browser.find_element(By.XPATH,locator.comm_member_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_set_admin).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm__admin_popup).is_displayed()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.comm_unsetadmin_exec).click()
    sleep(5)


@then(u'set and unset admin scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'set and unset admin scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
