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
       amount = str(item['quantity']) +" "+ str(units['label'])
       ingredient_info.update({food_info['label']:amount})
   return ingredient_info


def get_difficulty(recipe_list):
   difficulty_list = []
   for recipe_title in recipe_list:
       recipe = recipe_title['recipe']
       difficulty_list.append(recipe['level'])
   return difficulty_list


def main():
   ingredient = raw_input("Please input an ingredient ")
   recipe_list = call_api(ingredient)
   difficulty_list =  get_difficulty(recipe_list)
   recipe_names = get_recipe_title(recipe_list)
   for item in range(len(recipe_names)):
       print recipe_names[item], difficulty_list[item]
   chosen_recipe = choose_recipe(recipe_list)
   print get_recipe_ingredients(chosen_recipe)
   input()

main()
