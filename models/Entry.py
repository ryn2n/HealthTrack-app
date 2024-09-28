# An entry that exists one per day that is used to account for food and calories in a day
class Entry:
    def __init__(self, date, total_calories=0):
        self.date = date
        self.food_list = []
        self.total_calories = total_calories
    
    # TODO: Print Entry
    # TODO: Add a food
    # TODO: Get total calories (from food_list)
    # TODO: Get total protein (from food_list)
    # TODO: Remove a food