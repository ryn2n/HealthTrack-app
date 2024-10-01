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
            "<name> ..... (CFP) [N units]\n"
            "=========================\n"
            "--- FOODS IN DATABASE ---\n"
        )

        for food_name in food_dict:
            food_list += food_dict[food_name].print_food_inline() + "\n"
        food_list += "=========================\n\n"
        
        return food_list
    
    def show_food(self, name):
        # Validate food name exists
        if self.model.does_food_exist(name):
            return self.model.get_food(name).print()
        else:
            raise NameError(f"\"{name}\" is not in database. Add with:\n./app create_food {name}")
    
    # TODO:
    def get_food(self, name):
        pass
    
    # TODO:
    def get_printed_food(self, name):
        pass
    
    # TODO:
    def update_food(self, name, cal, units, vol, protein)
    
    def delete_food(self, name):
        # Validate food exists
        if self.model.does_food_exist(name):
            self.model.delete_food(name)
        else:
            raise NameError(f"\"{name}\" is not in database. Add with:\n./app create_food {name}")