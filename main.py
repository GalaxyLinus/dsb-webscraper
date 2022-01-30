import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import dsbdata

# print(kivy.__version__)
kivy.require("2.0.0")   

class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class BetterDSB(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        # add widgets
        self.window.add_widget(Label(
            text = "BetterDSB - DEBUG",
            color = "ghostwhite",
            font_size = 18
            ))
        
        url = "https://dsbmobile.de/data/3bede8c6-b557-47a3-a312-82f8a59982b6/7b0ff467-5495-42ba-835a-9215bc975f9c/7b0ff467-5495-42ba-835a-9215bc975f9c.html"
        
        klasse = "9"
        
        date = dsbdata.dsbdata.getVertretungen(data=dsbdata.dsbdata.getData(url=url), klasse=klasse)[1]
        
        output = "\n".join(dsbdata.dsbdata.getVertretungen(data=dsbdata.dsbdata.getData(url=url), klasse=klasse)[0])
        
        self.window.add_widget(Label(text = date))
        
        self.window.add_widget(Label(text = output))
        
        return self.window
        
        
        
if __name__ == "__main__":
    BetterDSB().run()