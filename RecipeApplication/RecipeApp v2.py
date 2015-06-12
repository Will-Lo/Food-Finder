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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<SearchScreen>:
	FloatLayout:
		Button:
			id: searchbutton
			text: 'Search!'
			pos_hint: {'center_x':0.5, 'center_y':0.3}
			size_hint: 0.4, 0.2
			on_press: 
				root.food_search()
				root.manager.transition.direction = 'left'
				root.manager.current = 'results'
		TextInput:
			id: textbox
			pos_hint: {'center_x':0.5, 'center_y':0.7}
			size_hint: 0.4,0.1
			multiline: False
			on_text_validate: 
				print self.text
				root.food_search()
				root.manager.transition.direction = 'left'
				root.manager.current = 'results'

				
<ResultsScreen>:
	on_pre_enter: root.show_results()
	GridLayout:
		padding:10
		cols:4
		rows:3
		Label:
			text_size: self.size
			text: root.title_list[0]
		Label:
			text_size: self.size
			text: root.title_list[1]
		Label:
			text_size: self.size
			text: root.title_list[2]
		Label:
			text_size: self.size
			text: root.title_list[3]
		Label:
			text_size: self.size
			text: root.title_list[4]
		Label:
			text_size: self.size
			text: root.title_list[5]
		Label:
			text_size: self.size
			text: root.title_list[6]
		Label:
			text_size: self.size
			text: root.title_list[7]
		Label:
			text_size: self.size
			text: root.title_list[8]
		Label:
			text_size: self.size
			text: root.title_list[9]
		Button:
			text: 'Go back to search'
			on_press:
				root.manager.transition.direction = 'right'
				root.manager.current = 'search'
''')		

recipe_list = [] #Global variable to keep all found recipes without repeated api calls

class SearchScreen(Screen):
	
	def food_search(self):
		global recipe_list
		food_input = self.ids.textbox.text
		recipe_list = call_api(food_input)

class ResultsScreen(Screen):

	title_list = ListProperty(['','','','','','','','','',''])
	
	def show_results(self):
		global recipe_list
		self.title_list = get_recipe_title(recipe_list)	
		print self.title_list
		
sm = ScreenManager()
sm.add_widget(SearchScreen(name='search'))
sm.add_widget(ResultsScreen(name='results'))

class RecipeScreen(Screen):
	pass
	
	
class RecipeApp(App):

	def build(self):
		return sm
		
if __name__=='__main__':
	RecipeApp().run()
	