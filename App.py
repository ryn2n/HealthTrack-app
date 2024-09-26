import sys
from controllers.weight_controller import WeightController
# from controllers.calorie_controller import CalorieController

# Example of initializing RESTful controllers
weight_controller = WeightController()
# calorie_controller = CalorieController()

# Run your app (REST server setup, etc.)

# Home
if (len(sys.argv) == 1): # In case using "$*" instead of "$@"
    weight_controller.home()
    return