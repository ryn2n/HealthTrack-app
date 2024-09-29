from models.food import Food
from models.food_model import FoodModel

class FoodService:
    def __init__(self):
        self.model = FoodModel()

    def create_food(self, name):
        if len("name") < 0:
            raise NameError("Name is too short")
        
        # Validate food exists
        if self.model.does_food_exist(name):
            raise NameError(f"\"{name}\" already exists in database")

        food = Food(name)
        self.model.save_food(food)