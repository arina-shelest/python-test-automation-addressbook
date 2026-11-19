import os
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if os.getenv("CI") == "true":
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
            self.wd = webdriver.Chrome(options=options)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if os.getenv("CI") == "true":
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
            self.wd = webdriver.Edge(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if os.getenv("CI") == "true":
                options.add_argument("--headless")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
            self.wd = webdriver.Firefox(options=options)
        else:
            raise Exception(f"Unsupported browser {browser}")
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
