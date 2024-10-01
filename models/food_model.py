import os
import json
from models.food import Food
from utils.file_handler import init_filename, load_data
from utils.menus import print_error

class FoodModel:
    def __init__(self):
        try:
            self.filename = init_filename("food")
        except NameError as e:
            print_error(e)
    
    def does_food_exist(self, name):
        data = load_data(self.filename)

        if name in data:
            return True
        else:
            return False
    
    def save_food(self, food):
        data = load_data(self.filename)
        with open(self.filename, 'w') as file:
            data[food.name] = food.serialize()
            json.dump(data, file, indent=4, sort_keys=True)

    def get_food(self, name):
        data = load_data(self.filename)
        return Food.make_food(data[name])
    
    def get_all_foods(self):
        # TODO: Create dict of all foods (as dict {name:Food}) using get_food()
        food_dict = load_data(self.filename)
        
        for name in food_dict:
            food_dict[name] = Food.make_food(food_dict[name])
        
        return food_dict