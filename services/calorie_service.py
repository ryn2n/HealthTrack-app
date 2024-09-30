import datetime
from models.calorie_model import CalorieModel
from models.calorie_entry import CalorieEntry
from models.food_model import FoodModel
from utils.menus import print_error

class CalorieService:
    def __init__(self):
        self.model = CalorieModel()
        self.food_model = FoodModel()
    
    def create_entry(self, date):
        date_created = 0
        if date.lower() == "today":
            date_created = datetime.date.today().strftime('%m/%d/%y')
        else:
            date_created = date
        
        # Validate Date
        self.check_date_format(date_created)
        if self.model.does_date_exist(date_created):
            raise NameError(f"Entry for \"{date}\" already exists.")

        new_entry = CalorieEntry(date_created)
        self.model.save_entry(new_entry)
        return date_created # Send date to cotroller for response message
    
    # Check if date is in proper format MM/DD/YY
    def check_date_format(self, date):
        try:
            datetime.datetime.strptime(date, '%m/%d/%y')
        except ValueError:
            raise NameError(f"\"{date}\" is not in the proper format \"MM/DD/YY\"")
    
    # Gets entry as CalorieEntry, Date should be in mm/dd/yy format
    def get_entry_by_date(self, date):
        if date.lower() == "today":
            date = datetime.date.today().strftime('%m/%d/%y')

        # Validate Date
        self.check_date_format(date)
        if not self.model.does_date_exist(date):
            raise NameError(f"Entry for \"{date}\" not found.")
        
        return self.model.get_entry(date)
    
    # Get entry in printed form - rely on get_entry_by_date
    def get_printed_entry(self, date):
        entry = self.get_entry_by_date(date)
        return entry.print()
    
    # TODO: validate arguments, process strings into lists
    def update_entry(self, date, total, add_foods, remove_foods):
        # Date is already validated when controller printed
        if date.lower() == "today":
            date = datetime.date.today().strftime('%m/%d/%y')
        entry = self.model.get_entry(date)
        
        if total == "": # In case no total was entered
            total = entry.total_calories

        # Validate total is a float
        try:
            float(total)
        except ValueError as e:
            raise NameError(e)

        # Get foods from string and Validate Foods exist in database
        foods_to_add = [food.strip() for food in add_foods.split(',')]
        added_foods = []
        for food in foods_to_add:
            if food == '': # If no food entered
                foods_to_add.remove('')
                continue
            if (not self.food_model.does_food_exist(food)):
                raise NameError(f"\"{food}\" is not in database. Add with ./app create_food {food}")
            added_foods.append(self.food_model.get_food(food))
        
        foods_to_remove = [food.strip() for food in remove_foods.split(',')]
        removed_foods = []
        for food in foods_to_remove:
            if food == '': # If no food entered
                foods_to_remove.remove('')
                continue
            if (not self.food_model.does_food_exist(food)):
                raise NameError(f"\"{food}\" is not in database. Add with ./app create_food {food}")
            removed_foods.append(self.food_model.get_food(food))
        
        # Update pulled entry
        entry.total_calories = total
        entry.add_foods(added_foods)
        entry.remove_foods(removed_foods)

        # TODO: Save entry back to data
        self.model.save_entry(entry)