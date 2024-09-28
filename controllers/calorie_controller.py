from services.calorie_service import CalorieService

class CalorieController:
    def __init__(self):
        self.service = CalorieService()
    
    def create_entry(self, date):
        date_created = self.service.create_entry(date)
        response = f"Entry created for: {date_created}"
        return response