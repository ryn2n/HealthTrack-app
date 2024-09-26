from services.weight_service import WeightService
from utils.menus import print_error
import datetime

# Receives commands and delivers response
class WeightController:
    def __init__(self):
        self.service = WeightService
    
    def home(self):
        response = (
            "Welcome to the App!\n"
            "\n"
            "Add New Weight: ./app add_weight <weight>\n"
            "Show Trends: ./app graph_weight [limit]  *note: optional limit, default is 30\n"
            "Help Page: ./app -h"
        )
        return response
    
    def add_weight(self, weight):
        current_date = datetime.datetime.today().replace(microsecond=0)
        self.service.add_weight(weight, current_date)
        
        response = (
            f"Weight {weight} added successfully on {current_date}\n"
            "\n"
            "Go back to Home: ./app"
        )
        return response
    
    def graph_weight(self, limit=30):
        print(f"Showing trend for all time and past {limit} entries...")
        self.service.graph_weight(limit)
        
        response = (
            "Window Closed.\n"
            "\n"
            "Go back to Home: ./app"
        )
        return response