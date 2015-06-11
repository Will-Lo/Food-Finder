import kivy
kivy.require('1.9.0')
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder

	
Builder.load_string('''
<Image_a>:
	AsyncImage:
		source:'https://www.edamam.com/web-img/8bb/8bb76a6852aa6383785f54c2445a628c.jpg'
''')

class Image_a(Widget):
	pass

class MyApp(App):
	def build(self):
		return Image_a()

if __name__=='__main__':
	MyApp().run()