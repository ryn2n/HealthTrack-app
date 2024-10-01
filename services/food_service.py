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
    
    # Prints all foods in list
    def list_foods(self):
        food_dict = self.model.get_all_foods()
        
        food_list = (
            "Format of foods:\n"
            "<FOOD> (CFP) [N units]\n"
            "\n"
            "--- FOODS IN DATABASE ---\n"
        )

        for food_name in food_dict:
            food_list += food_dict[food_name].print_food_inline() + "\n"
        food_list += "=========================\n\n"
        
        return food_list