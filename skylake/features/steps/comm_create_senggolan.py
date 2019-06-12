from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from database import*
from hamcrest import*

@given(u'create senggolan scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'create senggolan scenario - login as community owner')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'create senggolan scenario - go to community tab and find community')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.comm_north_tab).click()
    sleep(4)

@when(u'create senggolan scenario - create private project senggolan with four images')
def step_impl(context):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.senggolan_create).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_category).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_project).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_title).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.senggolan_title).send_keys(database.userdata["senggolan_title"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_desc).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_desc).send_keys(database.userdata["senggolan_desc"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_attc1).send_keys(os.path.join(project_dir, 'resource/husky.jpg'))
    context.browser.find_element(By.XPATH,locator.senggolan_attc2).send_keys(os.path.join(project_dir, 'resource/theodore.jpg'))
    context.browser.find_element(By.XPATH,locator.senggolan_attc3).send_keys(os.path.join(project_dir, 'resource/aerith.jpg'))
    context.browser.find_element(By.XPATH,locator.senggolan_attc4).send_keys(os.path.join(project_dir, 'resource/upin_ipin.jpg'))
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_pass).click()
    context.browser.find_element(By.XPATH,locator.senggolan_pass).send_keys(database.userdata["password"])
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_exec).click()
    sleep(8)


@then(u'create senggolan scenario - validating senggolan')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.senggolan_header).is_displayed()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_title_valid).is_displayed()
    sleep(2)
    title = context.browser.find_element(By.XPATH,locator.senggolan_title_valid)
    validation = title.text
    assert_that(validation, contains_string(database.userdata["senggolan_title"]))
    sleep(5)

@then(u'create senggolan scenario - delete senggolan')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.senggolan_option).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.senggolan_delete).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.popup).is_displayed()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.senggolan_delete_exec).click()
    sleep(5)


@then(u'create senggolan scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'create senggolan scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing).is_displayed()
