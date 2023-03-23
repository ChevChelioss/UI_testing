import allure


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Test filling out the practice form with valid data')
def test_valid_data_practice_form(practice_page, user):
    practice_page.fill(user).assert_results_registration(user)


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Test filling out the practice form with invalid email')
def test_invalid_email_practice_form(practice_page, user):
    user.email = 'invalidemail'
    practice_page.fill(user).assert_validation_email()


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Test filling out the practice form without required fields')
def test_empty_fields_practice_form(practice_page, user):
    practice_page.submit().assert_required_fields()


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Test filling out the practice form with invalid phone number')
def test_invalid_phone_practice_form(practice_page, user):
    user.phone = 'invalidphone'
    practice_page.fill(user).assert_validation_phone_number()


@allure.label('owner', 'Artur Gabdrakhmanov')
@allure.title('Test confirming the completion of the form for practice')
def test_unsupported_skin_practice_form(practice_page, user):
    practice_page.assert_validation_skin()
