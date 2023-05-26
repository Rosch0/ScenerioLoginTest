from behave import Given, When, Then, And
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open('TestProject/steps/data.json') as user_file:
    file_contents = json.load(user_file)

#Scenario: Unactive Log in button on empty fields
class LoginButton:
    @Given("I am on the login page 1")
    def step_impl(context):
        context.browser = webdriver.Chrome()
        context.browser.get("https://www.redbubble.com/auth/login")
        pass

    @When('I kill cookies')
    def step_I_kill_cooke(self, context):
        kill_cooke_click = context.browser.find_element(By.XPATH,'//*[@id="CybotCookiebotDialogBodyButtonDecline"]')
        kill_cooke_click.click()
        pass

    @And('The "Email" and "Password" field is empty')
    def step_impl(context):
        username_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput1"]')
        username_input.send_keys(' ')

        password_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput2"]')
        password_input.send_keys(' ')
        pass

    @Then('Log in button should be in disabled state')
    def button(context):
            login_button_click = context.browser.find_element(By.XPATH,'//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button')
            login_button_click.click()
            pass
        

#Scenario: Log in button state - bad Email syntax
class LoginButton2:
    @Given('I am on the login page 2')
    def step_impl(context):
        context.browser = webdriver.Chrome()
        context.browser.get("https://www.redbubble.com/auth/login")
        pass

    @When('I kill cookies 2')
    def step_I_kill_cooke(self, context):
        kill_cooke_click = context.browser.find_element(By.XPATH,'//*[@id="CybotCookiebotDialogBodyButtonDecline"]')
        kill_cooke_click.click()
        pass
    
    @And('I type "Bad Syntax Email" in Email Field')
    def button(context):
            username_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput1"]')
            username_input.send_keys(file_contents['Bad_username'])
            pass
    
    @And('I type "Registed User Pwd" in Passowrd Field 1')
    def password_place(context):
            password_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput2"]')
            password_input.send_keys(file_contents['Good_password'])
            pass

    @Then('Log in button should be in disabled state 1')
    def button(context):
            login_button_click = context.browser.find_element(By.XPATH,'//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button')
            login_button_click.click()
            pass

#Scenario: Log in button state - good Email syntax
class LoginButton3:
    @Given('I am on the login page 3')
    def step_impl(context):
        context.browser = webdriver.Chrome()
        context.browser.get("https://www.redbubble.com/auth/login")
        pass

    @When('I kill cookies 3')
    def step_I_kill_cooke(self, context):
        kill_cooke_click = context.browser.find_element(By.XPATH,'//*[@id="CybotCookiebotDialogBodyButtonDecline"]')
        kill_cooke_click.click()
        pass

    @And('I type "Good Syntax Email" in Email Field') 
    def button(context):
            username_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput1"]')
            username_input.send_keys(file_contents['Good_username'])
            pass

    @And('I type "Registed User Pwd" in Passowrd Field 2')
    def password_place(context):
            password_input = context.browser.find_element(By.XPATH,'//*[@id="ReduxFormInput2"]')
            password_input.send_keys(file_contents['Good_password'])
            pass

    @Then('Log in button should be in active state 2')
    def button(context):
            login_button_click = context.browser.find_element(By.XPATH,'//*[@id="RB_React_Component_LoginFormContainer_0"]/div/form/span/button')
            login_button_click.click()
            pass
