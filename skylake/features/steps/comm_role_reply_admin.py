from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'role reply admin scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'role reply admin scenario - login as community admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username6"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()


@then(u'role reply admin scenario - go to community tab and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(4)

@then(u'role reply admin scenario - reply post as account')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_name).send_keys(Keys.PAGE_DOWN + Keys.PAGE_DOWN)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_role).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_role_acc).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).send_keys(database.userdata["text"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).send_keys(Keys.PAGE_DOWN)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_exec).click()
    sleep(5)


@then(u'role reply admin scenario - validating post reply as account')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_reply_validation).is_displayed()
    role = context.browser.find_elements(By.XPATH,locator.comm_reply_validation)
    account = role[0].text
    assert_that(account, equal_to_ignoring_whitespace(database.userdata["account_validation2"]))
    sleep(4)


@then(u'role reply admin scenario - delete reply as account')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_reply_opt).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_reply_delete).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)


@then(u'role reply admin scenario - reply the same post as community admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_reply).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_role).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_role_comm).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).send_keys(database.userdata["text"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_editor).send_keys(Keys.PAGE_DOWN)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.comm_reply_exec).click()
    sleep(5)

@then(u'role reply admin scenario - validating post reply as community admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_reply_validation).is_displayed()
    role = context.browser.find_elements(By.XPATH,locator.comm_reply_validation)
    admin = role[0].text
    assert_that(admin, equal_to_ignoring_whitespace(database.userdata["role_validation"]))
    sleep(4)

@then(u'role reply admin scenario - delete reply as admin')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.comm_reply_opt2).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_reply_delete2).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)

@then(u'role reply admin scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'role reply admin scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
