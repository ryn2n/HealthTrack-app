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
    
    def get_printed_food(self, name):
        # Validate food name exists
        if self.model.does_food_exist(name):
            return self.model.get_food(name).print()
        else:
            raise NameError(f"\"{name}\" is not in database. Add with:\n./app create_food {name}")
    
    # TODO: ?
    def get_food(self, name):
        # Validate exists, then return Food object
        pass
    
    # TODO: Update food with string inputs from user
    def update_food(self, name, new_name, cal, units, vol, protein):
        # name is already validated
        food = self.model.get_food(name)

        # Validate inputs
        # If any fields are blank, default to original value
        if new_name == "":
            new_name = food.name
        if cal == "":
            cal = food.total_calories
        if units == "":
            units = food.units
        if vol == "":
            vol = food.total_vol
        if protein == "":
            protein = food.total_protein
        # validate cal, units, vol, protein are floats/ints - convert them
        try:
            float(cal)
            int(units)
            float(vol)
            float(protein)
        except ValueError as e:
            raise NameError(e)

        # TODO: if name != new_name, self.delete_food(name)
        # Delete old food if changing name
        if name != new_name:
            self.delete_food(name)
        
        # TODO: Update the pulled entry - entry.name = new_name
        food.name = new_name
        food.total_calories = cal
        food.units = units
        food.total_vol = vol
        food.total_protein = protein

        # TODO: Save updated entry to model with save function
        self.model.save_food(food)

        return new_name # for controller
    
    def delete_food(self, name):
        # Validate food exists
        if self.model.does_food_exist(name):
            self.model.delete_food(name)
        else:
            raise NameError(f"\"{name}\" is not in database. Add with:\n./app create_food {name}")