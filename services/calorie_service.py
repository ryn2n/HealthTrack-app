import datetime
from models.calorie_model import CalorieModel
from models.calorie_entry import CalorieEntry

class CalorieService:
    def __init__(self):
        self.model = CalorieModel()
    
    def create_entry(self, date):
        date_created = 0
        if date == "TODAY":
            date_created = datetime.date.today()
        else:
            date_created = datetime.datetime.strptime(date, '%m/%d/%y')
        
        self.model.validate_date(date_created)

        new_entry = CalorieEntry(date_created)
        self.model.save_entry(new_entry)
        return date_created # Send date to cotroller for response message