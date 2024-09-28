import os
import json
import datetime
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
                data[entry.date.strftime('%m/%d/%y')] = entry.serialize() # TODO
                json.dump(data, file, indent=4, sort_keys=True)
        else:
            print(entry.date)
            with open(self.filename, 'w') as file:
                data[entry.date.strftime('%m/%d/%y')] = entry.serialize() # TODO:
                json.dump(data, file, indent=4, sort_keys=True)
    
    def validate_date(self, date):
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
        if date.strftime('%m/%d/%y') in data: # TODO:
            raise NameError(f"Entry for {date} already exists.")