import csv
import os
import datetime
from utils.menus import print_error

# Manages all data handling to and from database
class WeightModel:
    def __init__(self, filename='weight_data_demo.csv'):
        if os.path.exists("filename.txt"): # retrieve filename for data to load
            with open("filename.txt", 'r') as file:
                self.filename = file.read()
        else:
            self.filename = filename # else default to demo
        
    def save_filename(self, filename):
        if os.path.exists("filename.txt"):
            self.filename = filename
            with open("filename.txt", 'w') as file:
                file.write(filename)
        else:
            print_error("filename.txt does not exist. Please create this file.")
    
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