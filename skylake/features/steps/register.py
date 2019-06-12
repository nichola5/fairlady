from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from pathlib import Path
from database import*
from datetime import datetime

@given(u'register scenario - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'register scenario - register as new user')
def step_impl(context):

    now = datetime.now()
    time = now.strftime("%m%d%H%M%S")
    com = "@email.com"

    context.browser.find_element(By.XPATH,locator.register).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.popup_register)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.reg_name).send_keys(database.userdata["reg_name"],time)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.reg_mail).send_keys(database.userdata["reg_mail"],time,com)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.reg_pass).send_keys(database.userdata["password"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.reg_cnfrmpass).send_keys(database.userdata["password"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.reg_execution).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.skip).click()

@then(u'register scenario - complete profile and set avatar')
def step_impl(context):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    project_dir = Path(ROOT_DIR).parent.parent

    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_sett).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar_up).send_keys(os.path.join(project_dir, 'resource/theodore.jpg'))
    sleep(1)
    context.browser.find_element(By.XPATH,locator.save_avatar).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.bio).click()
    sleep(1)
    context.browser.find_element(By.XPATH,locator.bio).send_keys(database.userdata["bio"])
    sleep(3)
    context.browser.find_element(By.XPATH,locator.save_prof).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.save_prof).send_keys(Keys.UP + Keys.UP + Keys.UP)
    sleep(1)
    context.browser.find_element(By.XPATH,locator.sebangsa_home).click()
    sleep(8)

@then(u'register scenario - make new post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_newpost).click()
    context.browser.find_element(By.XPATH,locator.editor_container)
    context.browser.find_element(By.XPATH,locator.editor_container).send_keys(database.userdata["text"])
    context.browser.find_element(By.XPATH,locator.editor_execution).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(8)

@then(u'register scenario - deleting post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.editor_menu).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_delete).click()
    sleep(2)
    context.browser.find_element(By.XPATH,locator.editor_pop)
    context.browser.find_element(By.XPATH,locator.editor_yesbtn).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)

@when(u'register scenario - logout')
def step_impl(context):
    sleep(3)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'register scenario - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
