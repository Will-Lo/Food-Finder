import requests
import json


def call_api(ingredient):
	# credentials for the api
	app_id = '089eb38f'
	app_key = '1c85c101570a08bde8d50b217d7ca2d9'
	
	info = {'q': ingredient, 'app_id': app_id, 'app_key': app_key}
	# calls the api
	response = requests.post('https://api.edamam.com/search', data=info)
	# uses json to decode the object from the website
	j = json.loads(response.text)
	# 'hits' is the key for all data related to the recipe
	recipe_list = j['hits']
	return recipe_list


def get_recipe_title(recipe_list):
	recipe_names = []
	
	# loops through the list of recipes
	for item in recipe_list:
		recipe = item['recipe']
		# adds the titles of the recipe to a list
		recipe_names.append(recipe['label'])
	return recipe_names


def choose_recipe(recipe_list, choice):
	chosen_recipe = recipe_list[choice]
	return chosen_recipe


def get_recipe_ingredients(chosen_recipe):
	r = chosen_recipe['recipe']
	ingredient_list = r['ingredients']
	ingredient_info = []
	food_amount = []
	# loops through every ingredient in the ingredient list
	for item in ingredient_list:
		food_info = item['food']
		units = item['measure']
		food = str(item['quantity']) + " " + str(units['label'])
		# appends the name of the ingredient in one list, and the units and measure in another list
		ingredient_info.append(food_info['label'])
		food_amount.append(food)
	return food_info, food_amount



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

def get_one_image(chosen_recipe):
	# used to find only 1 image faster
	r = chosen_recipe['recipe']
	image_link = r['image']
	return image_link

def get_url(recipe_list):
	url_list = []
	for recipe_title in recipe_list:
		recipe = recipe_title['recipe']
		url_list.append(recipe['url'])
	return url_list

def open_url(url):
	webbrowser.open(str(url))

import kivy
kivy.require('1.9.0')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.factory import Factory
from kivy.uix.image import Image
import webbrowser

Builder.load_string('''
<SearchScreen>:
	FloatLayout:
		Label:
			text: 'Search for a recipe by inputting ingredients:'
			font_size: 25
			pos_hint: {'center_x': 0.5, 'center_y': 0.85}
			size_hint: 0.6,0.2
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

<SmartButton>:
	text_size: self.size

<ResultsScreen>:
	on_pre_enter: root.show_results()		
	GridLayout:
		padding:10
		cols:4
		rows:3
		SmartButton:
			text: root.title_list[0]
			on_release: 
				self.find_ingredient_info(0)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[1]
			on_release: 
				self.find_ingredient_info(1)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[2]
			on_release: 
				self.find_ingredient_info(2)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[3]
			on_release: 
				self.find_ingredient_info(3)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[4]
			on_release: 
				self.find_ingredient_info(4)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[5]
			on_release: 
				self.find_ingredient_info(5)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[6]
			on_release: 
				self.find_ingredient_info(6)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[7]
			on_release: 
				self.find_ingredient_info(7)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[8]
			on_release: 
				self.find_ingredient_info(8)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		SmartButton:
			text: root.title_list[9]
			on_release: 
				self.find_ingredient_info(9)
				root.manager.transition.direction = 'left'
				root.manager.current = 'ingredients'
		Button:
			text: 'Go back to search'
			on_press:
				root.manager.transition.direction = 'right'
				root.manager.current = 'search'

<SmartLabel>:
	size_hint: 0.4, 0.2
	text_size: self.size

<RecipeScreen>:
	on_pre_enter:
		root.show_recipe()
		root.build_labels()
		root.build_image()
	box:box
	
	FloatLayout:
		Button:
			pos_hint:{'center_x':0.2, 'center_y':0.1}
			size_hint: 0.4,0.1
			text: 'Go back to results'
			on_release:
				root.manager.transition.direction = 'right'
				root.manager.current = 'results'
				root.wipe_list()
		Button:
			pos_hint:{'center_x': 0.2, 'center_y':0.8}
			size_hint: 0.4, 0.1
			text: 'Open recipe instructions'
			on_release:
				root.build_url()
			
		
		Label:
			pos_hint:{'center_x':0.7, 'center_y':0.9}
			size_hint: 0.4, 0.1
			text: 'Ingredients'
			font_size: 22	
		AsyncImage:
			pos_hint:{'center_x':0.2, 'center_y':0.5}
			source: root.image
			
		FloatLayout:
			id:box

<MainWidget>:
	screen_manager: screen_manager
	ScreenManager:
		id: screen_manager
		SearchScreen:
			id: search_screen
			name:'search'
			manager: screen_manager
		ResultsScreen:
			id: results_screen
			name: 'results'
			manager: screen_manager
		RecipeScreen
			id: recipe_screen
			name: 'ingredients'
			manager: screen_manager
				
''')

recipe_list = [] #Global variable to keep all found recipes without repeated api calls
index_choose = 0 #Global variable required to find information of recipe chosen


class SearchScreen(Screen):
	
	def food_search(self):
		global recipe_list
		# sets search query to be equal to the text in the textbox to be equal
		food_input = self.ids.textbox.text
		# sets a global variable to be equal to the api call of the ingredient
		recipe_list = call_api(food_input)

		
class SmartButton(Button):

	id_num = NumericProperty()
	
	def find_ingredient_info(self, id):
		# so the program knows which button is pressed to open the correct ingredients
		global index_choose
		index_choose = id
		
		
class ResultsScreen(Screen):

	title_list = ListProperty(['','','','','','','','','',''])
	
	def show_results(self):
		global recipe_list
		titles = get_recipe_title(recipe_list)
		for item in titles:
			# inserts an item into the beginning of the list in case there aren't enough search results
			self.title_list.insert(0,item)
		print self.title_list

class SrollLabels(FloatLayout):
	pass
		
class RecipeScreen(Screen):
	ingredient_list = ListProperty([])
	amount_list = ListProperty([])
	box = ObjectProperty(None)
	labels = ListProperty([])
	url_label = ListProperty([])
	image = StringProperty()
	
	def show_recipe(self):
		global index_choose
		global recipe_list
		i_list, a_list = get_recipe_ingredients(choose_recipe(recipe_list,index_choose))
		for x in range(len(i_list)):
			self.ingredient_list.append(i_list[x])
			self.amount_list.append(a_list[x])
		print self.ingredient_list

	def build_url(self, *args):
		global index_choose
		global recipe_list
		url = str(get_url(recipe_list)[index_choose])
		# opens the web page connected to the recipe
		webbrowser.open(url)
		
	def build_image(self):
		global index_choose
		global recipe_list
		self.image = get_one_image(choose_recipe(recipe_list,index_choose))
	
	def build_labels(self, *args):
		# adds labels to the screen equal to the number of ingredients specified in the recipe
		self.labels = [Label(
			name='Ingredient {}'.format(i),
			text_size = (400,None),
			text="%s ) " %(i+1) + self.ingredient_list[i] + " " + self.amount_list[i],
			size_hint=(0.2,0.1),
			pos_hint={'center_x':0.7,'center_y': 0.8-i*0.075}
			)for i in range(len(self.ingredient_list))]
		for i in range(len(self.ingredient_list)):
			self.box.add_widget(self.labels[i])

	def wipe_list(self):
		# deletes all data when back button is pressed so data doesn't conflict with another recipe
		for i in range(len(self.ingredient_list)):
			self.box.remove_widget(self.labels[i])
		self.ingredient_list[:] = []
		self.amount_list[:] = []
		self.url_label[:] = []
		
class MainWidget(FloatLayout):
	manager = ObjectProperty(None)


class RecipeApp(App):

	def build(self):
		return MainWidget()
	
		
if __name__=='__main__':
	RecipeApp().run()
	