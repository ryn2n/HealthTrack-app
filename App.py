import sys
import argparse
from utils.menus import print_error
from controllers.weight_controller import WeightController
# from controllers.calorie_controller import CalorieController

def main():
    # Initializing controllers
    weight_controller = WeightController()
    # calorie_controller = CalorieController()

    # Home by default
    if (len(sys.argv) == 1): # In case using "$*" instead of "$@"
        print(weight_controller.home())
        return

    # Argument parser and subparsers
    parser = argparse.ArgumentParser(description="HealthTrack App: Your personal health center!", exit_on_error=False)
    subparsers = parser.add_subparsers(dest="command") # go to .command

    # App parsers
    app_parser = subparsers.add_parser("home", help="Back to app home")
    
    # Weight parsers
    add_weight_parser = subparsers.add_parser("add_weight", help="Add a weight entry", exit_on_error=False)
    add_weight_parser.add_argument("weight", type=float, help="Weight to add")
    graph_weight_parser = subparsers.add_parser("graph_weight", help="Graph all weight entries", exit_on_error=False)
    graph_weight_parser.add_argument("limit", type=int, nargs='?', default=30, help="Graph all entries, and last <int> entries (default is all)")

    # Calorie parsers
    # add_calories_parser = subparsers.add_parser("add_calories", help="Add calorie entry")
    # add_calories_parser.add_argument("calories", type=int, help="Calories to add")
    # graph_calories_parser = subparsers.add_parser("graph_calories", help="Graph all calorie entries")

    # Match command to controller
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print_error(e)
        return

    match args.command:
        case "home":
            print(weight_controller.home())
        case "add_weight":
            print(weight_controller.add_weight(args.weight))
        case "graph_weight":
            print(weight_controller.graph_weight(args.limit))
        case _:
            parser.print_help()
            return

if __name__ == "__main__":
    main()