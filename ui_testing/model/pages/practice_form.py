from selene import have
from selene.support.shared import browser
from ui_testing.model.controls.checkboxes import CheckboxFactory
from ui_testing.model.controls.datepicker import DatepickerFactory
from ui_testing.model.controls.dropdown import DropdownFactory
from ui_testing.model.controls.radio import RadiobuttonFactory
from ui_testing.utils import path_to_file, config


class PracticePage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.7)"')
        return self

    def fill_name(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        return self

    def fill_contacts(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.phone)
        return self

    def select_gender(self, user):
        gender = RadiobuttonFactory(browser.all('[name=gender]'))
        gender.select_by_value(user.gender)
        return self

    def select_birthday(self, user):
        set_birthday = DatepickerFactory(browser.element('#dateOfBirthInput'))
        set_birthday.select_date(user.birthday)
        return self

    def input_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def select_hobbies(self, user):
        set_hobbies = CheckboxFactory(browser.all('[for^=hobbies-checkbox]'))
        set_hobbies.select(user.hobbies)
        return self

    def upload_picture(self, user):
        browser.element('#uploadPicture').set_value(path_to_file.create_path(user.image))
        return self

    def input_address(self, user):
        browser.element('#currentAddress').type(user.address)
        return self

    def select_state(self, user):
        set_state = DropdownFactory('#state')
        set_state.select(user.state)
        return self

    def select_city(self, user):
        set_city = DropdownFactory('#city')
        set_city.select(user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def fill(self, user):
        (self.fill_name(user)
         .fill_contacts(user)
         .select_gender(user)
         .select_birthday(user)
         .input_subject(user)
         .select_hobbies(user)
         .upload_picture(user)
         .input_address(user)
         .select_state(user)
         .select_city(user)
         .submit())
        return self

    def assert_results_registration(self, user):
        browser.element('.table').all('td').even.should(have.texts(
            user.first_name + ' ' + user.last_name,
            user.email,
            user.gender,
            user.phone,
            user.birthday.strftime(config.datetime_view_format),
            user.subject,
            user.hobbies,
            user.image,
            user.address,
            user.state + ' ' + user.city))
        return self
