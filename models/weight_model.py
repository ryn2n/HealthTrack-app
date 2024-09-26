import csv
import os
import datetime
from utils.menus import print_error

# Manages all data handling to and from database
class WeightModel:
    def __init__(self, filename='weight_data.csv'):
        self.filename = filename
    
    def save_weight(self, weight, date):
        with open(self.filename, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([date, weight])
    
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