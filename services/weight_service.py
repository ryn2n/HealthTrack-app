from models.weight_model import WeightModel
from utils.graph import plot_graph
from utils.menus import print_error

class WeightService:
    def __init__(self):
        self.model = WeightModel
    
    # Process and check weight, then save to model
    def add_weight(self, weight, date):
        if weight < 0:
            print_error("Value Error: Weight must be a positive float")
            return
        self.model.save_weight(weight, date)
    
    def graph_weight(self, limit):
        data = self.model.get_graphing_data()
        data_limited = data[(-limit):]
        plot_graph(data, data_limited)