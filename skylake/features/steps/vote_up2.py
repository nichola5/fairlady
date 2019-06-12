from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'vote up scenario b - opening sebangsa')
def step_impl(context):
    #context.browser.get(database.userdata["url"])
    context.browser.find_element(By.XPATH,locator.landing)

@when(u'vote up scenario b - login as bot_3')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.popup_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys(database.userdata["username3"])
    sleep(1)
    context.browser.find_element(By.XPATH,locator.form_password).send_keys(database.userdata["password"])
    context.browser.find_element(By.XPATH,locator.button_confirm).click()

@then(u'vote up scenario b - go to timeline and wait')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.XPATH,locator.timeline_tab).click()
    sleep(10)

@then(u'vote up scenario b - vote up post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_up).click()
    sleep(3)

@then(u'vote up scenario b - validating vote up post active')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_component).is_displayed()
    vote_stat = context.browser.find_element(By.XPATH,locator.vote_stat).text
    assert_that(vote_stat, equal_to(database.userdata["vote_up_after"]))
    sleep(2)

@then(u'vote up scenario b - unvote post')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.vote_up).click()
    sleep(3)

@then(u'vote up scenario b - validating vote up post back to default')
def step_impl(context):
    try:
        context.browser.find_element(By.XPATH,locator.vote_component)
        status = False
    except:
        status = True
    assert_that(status, equal_to(True))

    #card_1 = card[0].text
    #component = find_element_by_tag_name("class").get_attribute("img-stats__wrapper")
    #print(dir(card))
    #assert_that(card_1, is_not(equal_to(database.userdata["vote_up_cls"])))
    sleep(2)

@when(u'vote up scenario b - logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.timeline_tab).send_keys(Keys.UP)
    sleep(2)
    context.browser.find_element(By.XPATH,locator.avatar).click()
    sleep(3)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(3)

@then(u'vote up scenario b - direct to landing page')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.landing)
