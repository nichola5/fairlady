from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from database import*


@given(u'login and logout scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'login and logout scenario - login using username and password')
def step_impl(context):

    context.browser.find_element(By.XPATH, locator.button_login1).click()
    context.browser.find_element(By.XPATH, locator.popup_login)
    context.browser.find_element(By.XPATH, locator.form_username).send_keys(database.userdata["username"])
    sleep(1)
    context.browser.find_element(By.XPATH, locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH, locator.button_confirm).click()

@then(u'login and logout scenario - direct to homepage user')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar)

@when(u'login and logout scenario - user logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'login and logout scenario - direct to sebangsa landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
