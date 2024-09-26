from services.weight_service import WeightService

class WeightController:
    def __init__(self):
        print("Controller Created")
        self.service = WeightService