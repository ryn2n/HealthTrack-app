from models.food import Food

# An entry that exists one per day that is used to account for food and calories in a day
class CalorieEntry:
    def __init__(self, date, total_calories=0, food_list=[]):
        self.date = date # As a string MM/DD/YY -> if need datetime for graphing or order, then convert
        self.food_list = food_list
        self.total_calories = total_calories
    
    # Serialize Entry for storage in json
    def serialize(self):
        entry_dict = {}
        entry_dict["date"] = self.date
        entry_dict["total_calories"] = self.total_calories

        # Food objects can't be stored in json, so serialize food
        food_list_serialized = []
        for food in self.food_list:
            food_list_serialized.append(food.serialize())
        entry_dict["food_list"] = food_list_serialized
        return entry_dict

    # Import entry - could use strings for date instead of datetime to keep without module?
    def make_entry(dictionary):
        food_list = []
        for food in dictionary["food_list"]:
            food_list.append(Food.make_food(food))
        return CalorieEntry(dictionary["date"], dictionary["total_calories"], food_list)

    def print(self):
        entry = (
            "--------------------------------\n"
            f"ENTRY FOR: {self.date}\n"
            f"\tTotal Calories = {self.total_calories} cal\n"
            f"\tTotal Protein = WORK-IN-PROGRESS\n"
            "Foods Eaten:\n"
        )
        
        for food in self.food_list:
            # food.print_inline()
            entry += (f"\tFood: {food.name} ({food.total_calories * food.units} cal)\n")
        
        entry += ("--------------------------------")
        return entry

    # Add foods from list and recalculate total calories
    def add_foods(self, foods):
        for food in foods:
            self.food_list.append(food)
            print(f"Added \"{food.name}\"")
        self.calc_total_cals()

    # Remove foods from list and recalculate total calories
    def remove_foods(self, foods):
        for food in foods:
            for index, check_food in enumerate(self.food_list):
                if food.name == check_food.name:
                    self.food_list.pop(index)
                    print(f"Removed \"{food.name}\"")
                    break
            else:
                print(f"\"{food.name}\" not found")
        self.calc_total_cals()

    def calc_total_cals(self):
        total = 0
        for food in self.food_list:
            total += food.total_calories * food.units
        self.total_calories = total
        return total

    # TODO: Get total protein (from food_list)