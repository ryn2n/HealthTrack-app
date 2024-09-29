import json
import os

def init_filename(tracker_type):    
    if os.path.exists("filename.json"): # retrieve filename for data to load
        with open("filename.json", 'r') as file:
            data = json.load(file)
            return data[tracker_type] # should be set up as: {string:filename} 
    else:
        raise NameError("filename.json not found. Please create this file.")

def save_filename_to_json(tracker_type, filename):
    if os.path.exists("filename.json"):
        data = {}
        with open("filename.json", 'r') as file:
            data = json.load(file)
        with open("filename.json", 'w') as file:
            data[tracker_type] = filename
            json.dump(data, file, indent=4, sort_keys=True)
    else:
        raise NameError("filename.json not found. Please create this file.")

def load_data(filename):
    data = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    return data