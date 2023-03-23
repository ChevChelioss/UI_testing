from selene import have


class RadiobuttonFactory:

    def __init__(self, element):
        self.element = element

    def select_by_value(self, value):
        self.element.element_by(have.value(value)).element('..').click()