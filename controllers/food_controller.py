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
        try:
            response = self.service.list_foods()
        except NameError as e:
            return print_error(e)

        confirmation = (
            "Show specific Food: "
            "./app show_food <name>\n"
            "Go back to Home: ./app"
        )
        response += confirmation

        return response
    
    def show_food(self, name):
        try:
            printed_food = self.service.show_food(name)
        except NameError as e:
            return print_error(e)
        
        return printed_food
    
    def edit_food(self, name):
        # TODO: Check if food exists and Get - in try block
        try:
            food = self.service.get_printed_food(name)
        except NameError as e:
            return print_error(e)
        # TODO: Print Food before editing
        print(food)

        # TODO: Take input [NAME?, total_calories, units, total_vol, total_protein]
        new_name = input("Enter name: ")
        total_calories = input("Enter total calories: ")
        units = input("Enter number of servings: ")
        total_vol = input("Enter total volume: ")
        total_protein = input("Enter total protein: ")

        # TODO: Send inputs to service to update - in try block
        try:
            self.service.update_food(new_name, total_calories. units, total_vol, total_protein)
        except NameError as e:
            return print_error(e)

        # TODO: print [updated food shown below] and Food after editing
        return f"Food \"{name}\" successfully edited."
    
    def delete_food(self, name):
        try:
            self.service.delete_food(name)
        except NameError as e:
            return print_error(e)
        
        response = (
            f"\"{name}\" successfully deleted.\n"
            "\n"
            "Go back to Home: ./app"
        )
        return response