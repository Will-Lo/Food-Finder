import requests
import json


def call_api(ingredient):
	app_id = '089eb38f'
	app_key = '1c85c101570a08bde8d50b217d7ca2d9'
	info = {'q': ingredient, 'app_id': app_id, 'app_key': app_key}
	response = requests.post('https://api.edamam.com/search', data=info)
	j = json.loads(response.text)
	recipe_list = j['hits']
	return recipe_list


def get_recipe_title(recipe_list):
	recipe_names = []
	for title in recipe_list:
		recipe = title['recipe']
		recipe_names.append(recipe['label'])
	return recipe_names


def choose_recipe(recipe_list):
	choice = input("Call index # for recipe you like ")
	chosen_recipe = recipe_list[choice]
	return chosen_recipe


def get_recipe_ingredients(chosen_recipe):
	r = chosen_recipe['recipe']
	ingredient_list = r['ingredients']
	ingredient_info = {}
	for item in ingredient_list:
		food_info = item['food']
		units = item['measure']
		amount = str(item['quantity']) + " " + str(units['label'])
		ingredient_info.update({food_info['label']: amount})
	return ingredient_info


def get_difficulty(recipe_list):
	difficulty_list = []
	for recipe_title in recipe_list:
		recipe = recipe_title['recipe']
		difficulty_list.append(recipe['level'])
	return difficulty_list


def get_image(recipe_list):
	image_list = []
	for recipe_title in recipe_list:
		recipe = recipe_title['recipe']
		image_list.append(recipe['image'])
	return image_list


import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class SearchResult(Widget):
	pass


class Textbox(TextInput):
	def __init__(self):
		# ensures that important stuff isn't overwritten
		super(Textbox, self).__init__()

		self.info = TextInput(
			multiline=False,
			size_hint = (0.3,0.1),
			pos_hint = {'center_x':0.5, 'center_y': 0.6}
		)
	def on_enter(instance, value):
		print value.text
		return value.text

class SearchButton(FloatLayout):
	def __init__(self):
		# ensures that important stuff isn't overwritten
		super(SearchButton, self).__init__()

		self.info = Button(
			text="search",
			size_hint=(0.2, 0.1),
			pos_hint={'center_x': 0.5, 'center_y': 0.3}
		)
		self.food = ''
		
	def on_touch_down(self, touch):
		if self.collide_point:
			print 'Touched!'
			recipe_list = call_api(self.food)
			recipe_title = get_recipe_title(recipe_list)
			print recipe_title


class InputScreen(FloatLayout):
	def __init__(self):
		# ensures that important stuff isn't overwritten
		super(InputScreen, self).__init__()

		#create objects
		button = SearchButton()
		searchbox = Textbox()
		
		#add the widgets above
		self.add_widget(button.info)
		self.add_widget(searchbox.info)
		
		ingredient = searchbox.info.bind(on_text_validate=searchbox.on_enter)

		button.food = 'banana'
		button.info.bind(on_release=button.on_touch_down)
		
		
class RecipeApp(App):
	def build(self):
		return InputScreen()
		

if __name__ == '__main__':
	RecipeApp().run()