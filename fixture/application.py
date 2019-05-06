from selenium import webdriver

class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.base_url = base_url

    def open_home_page(self):
            wd = self.wd
            wd.get(self.base_url)

    def destroy(self):
            self.wd.quit()
