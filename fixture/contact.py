from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        wd = self.app.wd
        # open contact page
        self.open_add_contact_page()
        # fill contact form
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        if contact.bday:
            wd.find_element(By.NAME, "bday").click()
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        if contact.bmonth:
            wd.find_element(By.NAME, "bmonth").click()
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear:
            wd.find_element(By.NAME, "byear").click()
            wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        # return to home page
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
