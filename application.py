from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        wd = self.wd
        # open groups page
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        # return to groups page
        self.returns_to_groups_page()

    def returns_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, contact):
        wd = self.wd
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
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
