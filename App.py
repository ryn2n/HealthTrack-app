import sys
import argparse
from utils.menus import print_error, home
from controllers.weight_controller import WeightController
from controllers.calorie_controller import CalorieController
from controllers.food_controller import FoodController

def main():
    # Initializing controllers
    weight_controller = WeightController()
    calorie_controller = CalorieController()
    food_controller = FoodController()

    # Home by default
    if (len(sys.argv) == 1): # In case using "$*" instead of "$@"
        home()
        return

    # Argument parser and subparsers
    parser = argparse.ArgumentParser(description="HealthTrack App: Your personal health center!", exit_on_error=False)
    subparsers = parser.add_subparsers(dest="command") # go to .command

    # App parsers
    app_parser = subparsers.add_parser("home", help="Back to app home")
    dir_weight_parser = subparsers.add_parser("dir_weight", help="Shows filename where data is being accessed")
    dir_weight_parser.add_argument("-c","--change", type=str, nargs='?', help="Change filename where weight data is being accessed to <filename>")
    # TODO: Maybe separate view dir and change dir commands? maybe even create dir - adjust to profiles?
    
    # Weight parsers
    add_weight_parser = subparsers.add_parser("add_weight", help="Add a weight entry", exit_on_error=False)
    add_weight_parser.add_argument("weight", type=float, help="Weight to add") # TODO: catch this exception gracefully
    graph_weight_parser = subparsers.add_parser("graph_weight", help="Graph all weight entries", exit_on_error=False)
    graph_weight_parser.add_argument("limit", type=int, nargs='?', default=30, help="Graph all entries, and last <int> entries (default is all)")

    # Calorie parsers
    create_calorie_entry_parser = subparsers.add_parser("create_entry_cal", help="Create a new calorie entry for a date")
    create_calorie_entry_parser.add_argument("date", nargs='?', default="TODAY", help="Set date for creating calorie entry (default is today) <MM/DD/YY>")
    # TODO: Get entry by date to retrieve an entry
    show_calorie_entry_parser = subparsers.add_parser("show_entry_cal", help="Show a calorie entry for a date", exit_on_error=False)
    show_calorie_entry_parser.add_argument("date", help="Date of entry to show") # TODO: catch this exception gracefully
    # TODO: Update entry to update and edit a retrieved entry
    # TODO: Get all entries for graphing - so CRUD for entry?
    # graph_calories_parser = subparsers.add_parser("graph_calories", help="Graph all calorie entries")

    # Food parsers
    # TODO: Create food to add a food to database
    create_food_parser = subparsers.add_parser("create_food", help="Create a new Food in the database", exit_on_error=False)
    create_food_parser.add_argument("name", help="Name of food") # TODO: catch this exception gracefully
    # TODO: Show all foods to list all foods to add in database - so CRUD for food?
    # TODO: Update food
    # TODO: Delete food
    
    # Match command to controller
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print_error(e)
        return

    match args.command:
        case "home":
            print(weight_controller.home())
        case "dir_weight":
            print(weight_controller.change_dir(args.change))
        case "add_weight":
            print(weight_controller.add_weight(args.weight))
        case "graph_weight":
            print(weight_controller.graph_weight(args.limit))
        case "create_entry_cal":
            print(calorie_controller.create_entry(args.date))
        case "show_entry_cal":
            print(calorie_controller.show_entry(args.date))
        case "create_food":
            print(food_controller.create_food(args.name))
        case _:
            parser.print_help()
            return

if __name__ == "__main__":
    main()