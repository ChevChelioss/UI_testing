from datetime import date
import allure
from ui_testing.model.data.user import User
from ui_testing.model.pages.practice_form import PracticePage


@allure.title("Successful fill form")
def test_practice_form(user, practice_form):
    with allure.step('Open registrations form'):
        practice_form.open()
    with allure.step('Fill form'):
        practice_form.fill(user).submit()
    with allure.step('Check from results'):
        practice_form.assert_results_registration(user)
