# A food object for database
class Food:
    def __init__(self, name, total_calories=0, total_vol=0, total_protein=0):
        self.name = name
        self.total_calories = total_calories
        self.total_vol = total_vol
        self.total_protein = total_protein
    
    def serialize(self):
        food_dict = {}
        food_dict["name"] = self.name
        food_dict["total_calories"] = self.total_calories
        food_dict["total_vol"] = self.total_vol
        food_dict["total_protein"] = self.total_protein
        return food_dict

    def make_food(dictionary):
        return Food(dictionary["name"], dictionary["total_calories"], dictionary["total_vol"], dictionary["total_protein"])
    
    # TODO: Print Food
    # TODO: Set total calories
    # TODO: Set volume
    # TODO: Set protein