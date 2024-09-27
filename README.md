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
│
└── requirements.txt          # List of Python dependencies
```

## Necessary packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary libraries/packages.

### Needed libraries:
- matplotlib.pyplot

```bash
pip install matplotlib.pyplot
```

## How to use and run (EXAMPLE DELETE LATER)

Make sure that the /data/ folder is located in the same folder with all the scripts (this folder is not included).

To generate features in csv format in "features.csv", simply run the program using the command:
```bash
./run
```

The test program is used to verify that samples.csv has the correct output to features.csv, you need to first comment lines 46 and 55-62 and uncomment lines 48 and 65-71 in generate_rubine.py. Then, run the command:
```bash
./test
```

## Planned features

### Weight tracker:
Be able to edit or delete?
Trendline on graph?

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