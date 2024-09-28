# HealthTrack-app

## Project Structure
```
health_tracker/
│
├── app.py                   # Main entry point of the application
├── controllers/              # Contains RESTful route handlers
│   ├── __init__.py
│   ├── weight_controller.py  # Handles weight-related requests
│   └── calorie_controller.py # Handles calorie-related requests
│
├── services/                 # Business logic and service classes
│   ├── __init__.py
│   ├── weight_service.py     # Manages weight operations
│   └── calorie_service.py    # Manages calorie operations
│
├── models/                   # Data models and file operations
│   ├── __init__.py
│   ├── weight_model.py       # Handles storage for weight data
│   └── calorie_model.py      # Handles storage for calorie data
│
├── utils/                    # Utilities (e.g., graphing, logging)
│   ├── __init__.py
│   ├── graph.py              # Functions to graph weight/calories
│   └── file_handler.py       # File read/write utilities
|
├── tests/                    # Testing the application (empty for now)
│
└── requirements.txt          # List of Python dependencies
```

## Necessary packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary libraries/packages.

### Needed libraries:
- matplotlib.pyplot
- numpy

```bash
pip install matplotlib.pyplot
pip install numpy
```

## How to use and run (EXAMPLE DELETE LATER)

Ensure that the `weight_data.csv` file and the `filename.txt` file are present.

To start up the app, simply run the program using the command:
```bash
./app
```

## Planned features

### Weight tracker:
Be able to edit or delete?
Instead limit to last N entries, limit x axis to last N days - will need to use timedelta to 

### Calorie tracker, or Nutrition tracker?:
Add entires to dates
Edit entries to add foods to them, to increase
Graph total calories in same way as weight, with all time and number entries
Trendline on graph

Calorie Entry has
- Date
- Total calories
- List of foods with calorie count for breakdown
- Protein?

(useful md tool: https://markdownlivepreview.com/)