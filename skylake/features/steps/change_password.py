from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*

@given(u'password scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'password scenario - login as bot_two')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'password scenario - go to setting')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_sett).click()
    sleep(2)

@then(u'password scenario - go to password and change password')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.password).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.old_password).click()
    context.browser.find_element(By.XPATH,locator.old_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.new_password).click()
    context.browser.find_element(By.XPATH,locator.new_password).send_keys(database.userdata["password_chge"])
    context.browser.find_element(By.XPATH,locator.confirm_password).click()
    context.browser.find_element(By.XPATH,locator.confirm_password).send_keys(database.userdata["password_chge"])

@then(u'password scenario - saving new password')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.save_password).click()
    sleep(3)

@When(u'password scenario - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.sebangsa_home).click()
    sleep(5)


@then(u'password scenario - direct to sebangsa landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing).is_displayed()
    sleep(3)

@when(u'password scenario - relogin with new password')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password_chge"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'password scenario - back to user setting')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_sett).click()
    sleep(2)

@then(u'password scenario - go to password again')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.password).click()
    sleep(1)

@then(u'password scenario - change to default password')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.old_password).click()
    context.browser.find_element(By.XPATH,locator.old_password).send_keys(database.userdata["password_chge"])
    context.browser.find_element(By.XPATH,locator.new_password).click()
    context.browser.find_element(By.XPATH,locator.new_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.confirm_password).click()
    context.browser.find_element(By.XPATH,locator.confirm_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.save_password).click()
    sleep(3)

@When(u'password scenario - logout again')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.popup_login).is_displayed()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.sebangsa_home).click()
    sleep(5)

@then(u'password scenario - back to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
