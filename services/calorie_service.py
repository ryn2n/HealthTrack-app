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
        
        # Validate Date
        self.check_date_format(date_created)
        if self.model.does_date_exist(date_created):
            raise NameError(f"Entry for \"{date}\" already exists.")

        new_entry = CalorieEntry(date_created)
        self.model.save_entry(new_entry)
        return date_created # Send date to cotroller for response message
    
    # Check if date is in proper format MM/DD/YY
    def check_date_format(self, date):
        try:
            datetime.datetime.strptime(date, '%m/%d/%y')
        except ValueError:
            raise NameError(f"\"{date}\" is not in the proper format \"MM/DD/YY\"")
    
    # Gets entry as CalorieEntry, Date should be in mm/dd/yy format
    def get_entry_by_date(self, date):
        # Validate Date
        self.check_date_format(date)
        if not self.model.does_date_exist(date):
            raise NameError(f"Entry for \"{date}\" not found.")
        
        return self.model.get_entry(date)
    
    def get_printed_entry(self, date):
        entry = self.get_entry_by_date(date)
        return entry.print()