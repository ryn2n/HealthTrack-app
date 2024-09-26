from services.weight_service import WeightService
from utils.menus import print_error

class WeightController:
    def __init__(self):
        print("Controller Created")
        self.service = WeightService
    
    # TODO: Home print out?
    def home(self):
        print("Weight Controller: Home")
    
    # TODO:
    def add_weight(self, weight):
        print("WC: adding weight")
    
    # TODO:
    def graph_weight(self, limit=30):
        print(f"WC: graphing with {limit} entries.")