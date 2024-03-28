import json

with open(r'page_objects/saucedemo/saucedemoLocators.json') as locators:
    locator = json.load(locators)

class sauceLoginPage:
    def __init__(self,page):
        self.page = page
        
    def open(self):
        self.page.goto("https://www.saucedemo.com/")
    def sauceLoginLoad(self):
        self.page.is_visible(locator["loginlogo"])
        
    def sauceLogin(self):
        self.page.fill(locator["username"], 'standard_user')
        self.page.fill(locator["password"], 'secret_sauce')
        self.page.click(locator["loginbtn"])


