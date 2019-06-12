from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*

@given(u'change name scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'change name scenario - login using bot_two')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username2"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'change name scenario - go to user setting')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.usr_name).click()
    sleep(2)

@then(u'change name scenario - delete existing name and change full name')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.usr_name).send_keys(Keys.CONTROL + "a")
    context.browser.find_element(By.XPATH,locator.usr_name).send_keys(Keys.DELETE)
    context.browser.find_element(By.XPATH,locator.usr_name).send_keys(database.userdata["username_chg"])
    sleep(2)

@then(u'change name scenario - save profile and back to timeline')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.save_prof).click()
    sleep(7)
    context.browser.find_element(By.XPATH,locator.save_prof).send_keys(Keys.UP + Keys.UP + Keys.UP)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.sebangsa_home).click()
    sleep(5)

@When(u'change name scenario - open setting and logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'change name scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
