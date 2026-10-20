from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from contact import Contact


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_full_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd, Contact("John", "Smith", "Engineer",
                                        "Meta", "test@mail.com", "11",
                                        "October", "1986"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_contact_mandatory_fields(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd, Contact(firstname="Jack", lastname="Lu", email="test1@mail.com"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create_contact(self, wd, contact):
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

    def open_add_contact_page(self, wd):
        wd.find_element(By.LINK_TEXT, "add new").click()

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
