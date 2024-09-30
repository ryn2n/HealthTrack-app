from services.food_service import FoodService
from utils.menus import print_error

class FoodController:
    def __init__(self):
        self.service = FoodService()
    
    def create_food(self, name):
        try:
            self.service.create_food(name)
        except NameError as e:
            return print_error(e)
        
        response = f"Food created with name: {name}"
        return response