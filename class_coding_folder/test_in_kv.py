from kivy.app import App
from kivy.lang import Builder

class TestApp(App):
    item_to_price = {"Cheese": 12.50, "Laptop": 912.95,"Plant": 4.75}
    total = 0.0
    def build(self):
        self.title = "Kivy"
        self.root = Builder.load_file("test.kv")
        return self.root

    def on_button_press(self, button):
        self.total += self.item_to_price[button.text]
        self.root.ids.price_label.text = f"Total: ${self.total}"

    def on_reset_press(self,button):
        self.total = 0
        self.root.ids.price_label.text = "Total: $0.00"


TestApp().run()