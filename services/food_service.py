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
    
    # TODO: Prints all foods in list
    """
    Format of foods:
    FOOD (CFP) [N units]

    --- FOODS IN DATABASE ---
    Egg ..... (123 cal, 42g protein) [2 units]
    Eggplant ..... (123 cal, 42g protein) [1 unit]
    Beef ..... (123 cal, 42g protein) [1 unit]
    =========================
    """
    def list_foods(self):
        # TODO: Get food data from model
        food_dict = self.model.get_all_foods()
        
        # TODO: for Food in dict, print_inline food, collect and form into a response
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