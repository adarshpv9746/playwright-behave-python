import json

with open(r'page_objects/orange/orangeLocators.json') as locators:
    locator = json.load(locators)

class orangeLoginPage:
    def __init__(self,page):
        self.page = page
    
    def open(self, url):
        print(url)
        self.page.goto(url)

    def orangeLoginCreds(self, username, password):
        self.page.fill(locator["username"], username)
        self.page.fill(locator["password"], password)
        
    def orangeLogin(self):  
        print("user clicks login")  
        self.page.click(locator["loginbtn"])
        
    def orangeValidation(self):
        print("Validating dashboard")
        self.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")\
            
    def orangeLogout(self):
        print('logout')
        self.page.click('//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p')
        self.page.click('//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
    
    

