from services.weight_service import WeightService
from utils.menus import print_error
import datetime

# Receives commands and delivers response
class WeightController:
    def __init__(self):
        self.service = WeightService()
    
    def change_dir(self, filename):
        # Catch if filename cannot be created
        try:    
            self.service.change_filename(filename)
        except NameError as e:
            print_error(e)
            return
        
        return f"File being accessed set to: {self.service.get_filename()}"
    
    def add_weight(self, weight):
        current_date = datetime.datetime.today().replace(microsecond=0)
        
        try:
            self.service.add_weight(weight, current_date)
        except NameError as e:
            print_error(e)
            return
        
        response = (
            f"Weight {weight} added successfully on {current_date}\n"
            "\n"
            "Go back to Home: ./app"
        )
        return response
    
    def graph_weight(self, limit=30):
        print(f"Showing trend for all time and past {limit} entries...\n")
        self.service.graph_weight(limit)
        
        response = (
            "Window Closed.\n"
            "\n"
            "Go back to Home: ./app"
        )
        return response