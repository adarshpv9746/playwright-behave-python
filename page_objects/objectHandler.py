from page_objects.saucedemo.sauceLogin import sauceLoginPage
from page_objects.orange.orangeLogin import orangeLoginPage

class ObjectHandler:
    def __init__(self, page):
        self.page = page
        self.sauceloginpage = sauceLoginPage(self.page)
        self.orangeLoginpage = orangeLoginPage(self.page)

    def sauceLogin_page_init(self):
        return self.sauceloginpage

    def orangeLogin_page_init(self):
        return self.orangeLoginpage