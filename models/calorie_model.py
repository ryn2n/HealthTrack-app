import os
import json
from models.calorie_entry import CalorieEntry
from utils.menus import print_error
from utils.file_handler import init_filename, load_data

class CalorieModel:
    def __init__(self):
        try:
            self.filename = init_filename("calorie")
        except NameError as e:
            print_error(e)
    
    def save_entry(self, entry):
        data = load_data(self.filename)
        with open(self.filename, 'w') as file:
            data[entry.date] = entry.serialize()
            json.dump(data, file, indent=4, sort_keys=True)

    def does_date_exist(self, date):
        data = load_data(self.filename)
        
        if date in data:
            return True
        else:
            return False

    def get_entry(self, date):
        data = load_data(self.filename)
        return CalorieEntry.make_entry(data[date])