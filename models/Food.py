# A food object for database
class Food:
    def __init__(self, name, total_calories=0, units=1, total_vol=None, total_protein=None):
        self.name = name
        self.total_calories = total_calories
        self.units = units
        self.total_vol = total_vol
        self.total_protein = total_protein
    
    def serialize(self):
        food_dict = {}
        food_dict["name"] = self.name
        food_dict["total_calories"] = self.total_calories
        food_dict["units"] = self.units
        food_dict["total_vol"] = self.total_vol
        food_dict["total_protein"] = self.total_protein
        return food_dict

    def make_food(dictionary):
        return Food(dictionary["name"], dictionary["total_calories"], dictionary["units"], dictionary["total_vol"], dictionary["total_protein"])
    
    # Print Food Object with all stats
    def print(self):
        food = (
            "=======================\n"
            "--- Nutrition Facts ---\n"
            f"{self.name}\n"
            f"Servings = {self.units}\n"
            f"Calories = {self.total_calories} cal\n"
            f"Protein = {self.total_protein} g\n"
            f"Total Volume = {self.total_vol} g\n"
            "======================="
        )
        return food
    
    # Print Food object in one line
    # Food (CFP) [n units]
    # Egg ..... (123 cal, 42g protein) [1 unit]
    def print_food_inline(self):
        food = f"{self.name} ..... ({self.total_calories} cal) [{self.units}"
        if self.units > 1:
            food += " units]"
        else:
            food += " unit]"
        return food

    # TODO: Set total calories
    # TODO: Set volume
    # TODO: Set protein
    # TODO: Set units