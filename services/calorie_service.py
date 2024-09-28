import datetime
from models.calorie_model import CalorieModel
from models.calorie_entry import CalorieEntry

class CalorieService:
    def __init__(self):
        self.model = CalorieModel()
    
    def create_entry(self, date):
        date_created = 0
        if date == "TODAY":
            date_created = datetime.datetime.today()
        else:
            date_created = datetime.strptime(date, '%m/%d/%y')
        
        # TODO: Confirm that this date is valid (there is not already an entry for today)
        new_entry = CalorieEntry(date)
        self.model.save_entry(new_entry)
        return date_created # Send date to cotroller for response message