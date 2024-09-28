from services.calorie_service import CalorieService
from utils.menus import print_error

class CalorieController:
    def __init__(self):
        self.service = CalorieService()
    
    def create_entry(self, date):
        try:
            date_created = self.service.create_entry(date)
        except NameError as e:
            print_error(e)
            return
            
        response = f"Entry created for: {date_created}"
        return response