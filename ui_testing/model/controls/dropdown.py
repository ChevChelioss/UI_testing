from selene import have
from selene.support.shared import browser


class DropdownFactory:

    def __init__(self, selector):
        self.selector = selector

    def select(self, by_text):
        browser.element(self.selector).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(by_text)).click()