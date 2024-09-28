import csv
import os
import datetime
from utils.menus import print_error
from utils.filename import init_filename, save_filename_to_json

# Manages all data handling to and from database
class WeightModel:
    def __init__(self):
        self.filename = init_filename("weight")
        
    def save_filename(self, filename):
        save_filename_to_json("weight", filename)
        self.filename = filename
    
    def save_weight(self, weight, date):
        if os.path.exists(self.filename):
            with open(self.filename, 'a') as file:
                writer = csv.writer(file)
                writer.writerow([date, weight])
        else:
            raise NameError(f"{self.filename} does not exist")
    
    def get_graphing_data(self):
        # Retrieve Data
        data = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                data = [(datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"), float(row[1])) for row in reader]
        else:
            print_error(f"{self.filename} does not exist.")
        return data