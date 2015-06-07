import kivy
kivy.require('1.9.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<SearchButton>:
	FloatLayout:
		Button:
			text: 'Search!'
			pos_hint: {'center_x':0.5, 'center_y':0.3}
			size_hint: 0.4, 0.2
			on_press: print "Hi"

<TextBox>:
	FloatLayout:
		TextInput:
			pos_hint: {'center_x':0.5, 'center_y':0.7}
			size_hint: 0.4,0.1
			multiline: False
			on_text_validate: print self.text
				
			
''')

class SearchButton(FloatLayout):
	pass

class TextBox(FloatLayout):
	pass

class RecipeApp(App):

	def build(self):
		root = FloatLayout()
		button = SearchButton()
		textbox = TextBox()
		
		root.add_widget(button)
		root.add_widget(textbox)
		
		return root
		
if __name__=='__main__':
	RecipeApp().run()