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
    
    def list_foods(self):
        # Nothing to validate?
        # TODO: Place request to service in try block
        # return a message? "List completed"? ""
        try:
            response = self.service.list_foods()
        except NameError as e:
            return print_error(e)

        confirmation = (
            "Show specific Food:\n"
            "./app show_food <name>\n\n"
            "Go back to Home: ./app"
        )
        response += confirmation

        return response