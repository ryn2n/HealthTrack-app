import os
import json
from models.calorie_entry import CalorieEntry
from utils.menus import print_error
from utils.filename import init_filename

class CalorieModel:
    def __init__(self):
        try:
            self.filename = init_filename("calorie")
        except NameError as e:
            print_error(e)
    
    def save_entry(self, entry):
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
            with open(self.filename, 'w') as file:
                data[entry.date] = entry.serialize()
                json.dump(data, file, indent=4, sort_keys=True)
        else:
            with open(self.filename, 'w') as file:
                data[entry.date] = entry.serialize()
                json.dump(data, file, indent=4, sort_keys=True)
    
    # TODO: Hey isn't this completely reusable everywhere?
    # Loads in all the data from json and returns dict
    def load_data(self, filename):
        data = {}
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        return data

    def does_date_exist(self, date):
        data = self.load_data(self.filename)
        
        if date in data:
            return True
        else:
            return False

    def get_entry(self, date):
        data = self.load_data(self.filename)
        return CalorieEntry.make_entry(data[date])