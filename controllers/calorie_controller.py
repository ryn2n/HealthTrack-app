from services.calorie_service import CalorieService
from utils.menus import print_error

class CalorieController:
    def __init__(self):
        self.service = CalorieService()
    
    def create_entry(self, date):
        try:
            date_created = self.service.create_entry(date)
        except NameError as e:
            return print_error(e)
            
        response = f"Entry created for: {date_created}"
        return response
    
    def show_entry(self, date):
        try:
            printed_entry = self.service.get_printed_entry(date)
        except NameError as e:
            return print_error(e)
        
        return printed_entry
    
    def edit_entry(self, date):
        try:
            entry = self.service.get_printed_entry(date) # TODO: Is it inefficient to get object to print, and get again when updating? Or should I pass object through?
        except NameError as e:
            return print_error(e)
        print(entry)

        total_calories = input("Enter total calories: ")
        print("-- Note: Adding/Removing Foods will recalculate total calories --")
        foods_to_add = input("Enter foods to add, separated by ', ': ")
        foods_to_remove = input("Enter foods to remove, separated by ', ': ")

        try:
            self.service.update_entry(date, total_calories, foods_to_add, foods_to_remove)
        except NameError as e:
            return print_error(e)
        
        print()
        print("[updated entry shown below]")
        print(self.service.get_printed_entry(date))

        return f"Entry for {date} successfully edited."