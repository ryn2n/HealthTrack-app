import datetime
from models.calorie_model import CalorieModel
from models.calorie_entry import CalorieEntry

class CalorieService:
    def __init__(self):
        self.model = CalorieModel()
    
    def create_entry(self, date):
        date_created = 0
        if date == "TODAY": # TODO: Catch potential value error gracefully
            date_created = datetime.date.today().strftime('%m/%d/%y')
        else:
            date_created = date
        
        self.model.validate_date(date_created)

        new_entry = CalorieEntry(date_created)
        self.model.save_entry(new_entry)
        return date_created # Send date to cotroller for response message
    
    # Date should be in mm/dd/yy format
    def get_entry_by_date(self, date):
        pass
        selected_date = datetime.datetime