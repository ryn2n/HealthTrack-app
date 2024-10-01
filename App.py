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
    show_calorie_entry_parser = subparsers.add_parser("show_entry_cal", help="Show a calorie entry for a date", exit_on_error=False)
    show_calorie_entry_parser.add_argument("date", nargs='?', default="today", help="Date of entry to show, default today") # TODO: catch this exception gracefully
    edit_calorie_entry_parser = subparsers.add_parser("edit_entry_cal", help="Edit a calorie entry for a date")
    edit_calorie_entry_parser.add_argument("date", nargs='?', default="today", help="Date of entry to edit, default today") # TODO: catch this exception gracefully
    # TODO: add units to food when editing? or when adding?
    # TODO: Get all entries for graphing - so CRUD for entry?
    # graph_calories_parser = subparsers.add_parser("graph_calories", help="Graph all calorie entries")

    # Food parsers
    # TODO: adjust create to optionally add food in one line CLI - according to ipad
    create_food_parser = subparsers.add_parser("create_food", help="Create a new Food in the database", exit_on_error=False)
    create_food_parser.add_argument("name", help="Name of food") # TODO: catch this exception gracefully
    list_foods_parser = subparsers.add_parser("list_food", help="Show all Foods in the database", exit_on_error=False)
    show_food_parser = subparsers.add_parser("show_food", help="Show a Food by name", exit_on_error=False)
    show_food_parser.add_argument("name", help="Name of food") # TODO: catch this exception gracefully
    edit_food_parser = subparsers.add_parser("edit_food", help="Edit a Food by name", exit_on_error=False)
    edit_food_parser.add_argument("name", help="Name of food") # TODO: catch this exception gracefully
    delete_food_parser = subparsers.add_parser("delete_food", help="Delete a Food by name", exit_on_error=False)
    delete_food_parser.add_argument("name", help="Name of food") # TODO: catch this exception gracefully
    
    # Match command to controller
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print_error(e)
        return
    except SystemExit:
        print_error("Missing arguments.") # TODO: I don't think this is proper error handling
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
            print(calorie_controller.show_entry(args.date)) # TODO: when these try catch goes off, None is printed, potential remove print statement
        case "edit_entry_cal":
            print(calorie_controller.edit_entry(args.date))
        case "create_food":
            print(food_controller.create_food(args.name))
        case "list_food":
            print(food_controller.list_foods())
        case "show_food":
            print(food_controller.show_food(args.name))
        case "edit_food":
            print(food_controller.edit_food(args.name))
        case "delete_food":
            print(food_controller.delete_food(args.name))
        case _:
            parser.print_help()
            return

if __name__ == "__main__":
    main()