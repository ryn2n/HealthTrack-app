import datetime

# An entry that exists one per day that is used to account for food and calories in a day
class CalorieEntry:
    def __init__(self, date, total_calories=0, food_list=[]):
        self.date = date
        self.food_list = food_list
        self.total_calories = total_calories
    
    # Serialize Entry for storage in json
    def serialize(self):
        entry_dict = {}
        entry_dict["date"] = self.date.strftime('%m/%d/%y')
        entry_dict["food_list"] = self.food_list
        entry_dict["total_calories"] = self.total_calories
        return entry_dict

    # TODO: Import Entry
    def make_entry(self, dictionary):
        return CalorieEntry(datetime.datetime.strptime(dictionary["date"], '%m/%d/%y'), dictionary["total_calories"], dictionary["food_list"])

    # TODO: Print Entry
    # TODO: Add a food - call get total each time?
    # TODO: Get total calories (from food_list) - have this recalculate and replace existing total when called
    # TODO: Get total protein (from food_list)
    # TODO: Remove a food