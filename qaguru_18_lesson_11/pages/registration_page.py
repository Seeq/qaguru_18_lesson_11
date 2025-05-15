from time import sleep
from selene import browser, be, have
import os


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_phone = browser.element('#userNumber')
        pass

    def open(self):
        browser.open('/automation-practice-form')
        sleep(2)
        browser.element('#fixedban').should(be.visible)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('header').remove()")
        return self

    def preconditions_met(self):
        browser.element('#app').should(be.visible)
        browser.element('#app').should(have.text('Practice Form'))
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('select').element(f'option[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--{day}').click()
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.user_email.type(value)
        return self

    def select_gender(self):
        browser.element('[for="gender-radio-1"]').click()
        return self

    def fill_user_phone(self, value):
        self.user_phone.type(value)
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()
        return self

    def upload_img(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'files', 'meme.png'))
        browser.element('input[type="file"]').set_value(file_path)
        return self

    def fill_address(self,value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self):
        browser.element('#state').click()
        browser.element('#react-select-3-option-3').click()
        return self

    def select_city(self):
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').click()
        return self

    def click_submit_button(self):
        browser.element('#submit').click()
        return self




    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth, language, hobbies, photo, address, city):
        browser.element('.table').all('td:nth-child(2)').should(have.exact_texts(
            full_name,
            email,
            gender,
            phone,
            date_of_birth,
            language,
            hobbies,
            photo,
            address,
            city))
        return self
