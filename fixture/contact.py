import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_elements(By.NAME, "selected[]")[index].click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, new_contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact)
        # submit creation
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.XPATH, "//img[@title='Details']")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("email", contact.email)
        self.change_field_value("byear", contact.byear)
        if contact.bday:
            self.select_option("bday", contact.bday)
        if contact.bmonth:
            self.select_option("bmonth", contact.bmonth)

    def select_option(self, field_name, text):
        wd = self.app.wd
        Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                text_firstname = cells[2].text
                text_lastname = cells[1].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(
                    Contact(firstname=text_firstname, lastname=text_lastname, id=id,
                            all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails,
                            address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, email=email, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone)
