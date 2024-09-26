# HealthTrack-app

Trying out project structure:

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
