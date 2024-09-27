import os
from models.weight_model import WeightModel
from utils.graph import plot_graph_weight
from utils.menus import print_error

# Handles all function, logic check values, asks model for data
class WeightService:
    def __init__(self):
        self.model = WeightModel()
    
    def get_filename(self):
        return self.model.filename
    
    def change_filename(self, filename):
        if filename and os.path.exists(filename):
            self.model.save_filename(filename)
            return 0 # For success
        else:
            return 1 # For fail, like cpp program exit
    
    # Process and check weight, then save to model
    def add_weight(self, weight, date):
        if weight < 0:
            print_error("Value Error: Weight must be a positive float")
            return
        self.model.save_weight(weight, date)
    
    def graph_weight(self, limit):
        data = self.model.get_graphing_data()
        plot_graph_weight(data, limit)