from models.weight_model import WeightModel
from utils.graph import plot_graph

class WeightService:
    def __init__(self):
        print("Service Created")
        self.model = WeightModel