## Проект Ui_testing
##### Данный проект представляет собой ряд автотестов для проверки функциональности формы регистрации на сайте https://demoqa.com. 
Автотесты написаны на языке Python с использованием библиотеки pytest и фреймворка Selene для работы с Selenium WebDriver.

<!-- Технологии -->

### Используемые технологии
<p  align="center">
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/python.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/pytest.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/pycharm.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/selene.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_testops.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_report.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jenkins.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/selenium.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jira.png"></code>
</p>

### Для запуска тестов необходимо установить следующие зависимости:

- Python 3
- Библиотеки pytest, selenium, selene, allure-pytest
- WebDriver для браузера Chrome
- Приложение Allure для формирования отчетов

### Для проверки корректности заполнения формы были написаны следующие тесты:
- Тест на заполнение формы с правильными данными
- Тест на заполнение формы с неправильным email
- Тест на заполнение формы без заполнения обязательных полей
- Тест на заполнение формы с неправильным номером телефона
- Тест на подтверждение завершения заполнения формы
