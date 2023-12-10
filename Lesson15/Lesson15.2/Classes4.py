clicks = 0
class Button:
    def __init__(self):
        self.click_count = 0
    def click(self):
        self.click_count += 1
    def get_click_count(self):
        return self.click_count

a = Button()
a.click()
a.click()
print(a.get_click_count())