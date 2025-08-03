from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import json
import random

class QuoteBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text="Tap below to show a random quote!", size_hint=(1, 0.8), halign='center', valign='middle')
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.label)

        btn = Button(text="Get Random Quote", size_hint=(1, 0.2))
        btn.bind(on_press=self.show_quote)
        self.add_widget(btn)

        # Load quotes from file
        with open("..assets/quotes_100.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.quotes = data.get("quotes", [])

    def show_quote(self, instance):
        quote = random.choice(self.quotes)
        self.label.text = f'"{quote["quote"]}"\n\n— {quote["author"]}'

class QuoteApp(App):
    def build(self):
        return QuoteBox()

if __name__ == "__main__":
    QuoteApp().run()



