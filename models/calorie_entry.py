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
        entry_dict["food_list"] = self.food_list
        entry_dict["total_calories"] = self.total_calories
        return entry_dict

    # Import entry - could use strings for date instead of datetime to keep without module?
    def make_entry(dictionary):
        return CalorieEntry(dictionary["date"], dictionary["total_calories"], dictionary["food_list"])

    # TODO: Print Entry
    '''
    --------------------------------
    ENTRY FOR: 09/28/24
        Total Calories = 2200.0 cal
        Total Protein = 100.0 g
    Foods Eaten:
        Bread (130 cal, 10 g)
        Chipotle (800 cal, 50 g)
        Piada (1000 cal, 40 g)
    ---------------------------------
    '''
    def print(self):
        entry = (
            "--------------------------------\n"
            f"ENTRY FOR: {self.date}\n"
            f"\tTotal Calories = {self.total_calories} cal\n"
            f"\tTotal Protein = self.get_total_protein()\n"
            "Foods Eaten:\n"
        )
        
        for food in self.food_list:
            # food.print_inline()
            entry += (f"\tFood: {food}")
        
        entry += ("--------------------------------")
        return entry

    # TODO: Add a food - call get total each time?
    # TODO: Get total calories (from food_list) - have this recalculate and replace existing total when called
    # TODO: Get total protein (from food_list)
    # TODO: Remove a food