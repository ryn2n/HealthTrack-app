def print_error(message):
    print("Uh oh! Error found.")
    print()
    print(message)
    print()
    print("Go back to Home: ./app")

def home():
    menu = (
        "Welcome to the App!\n"
        "\n"
        "Add New Weight: ./app add_weight <weight>\n"
        "Show Weight Trends: ./app graph_weight [limit]  *note: optional limit, default is 30\n"
        "Weight Data Directory: ./app dir_weight [--change <filename>]\n"
        "Create New Entry: ./app create_entry_cal [date]\n"
        "Show Entry for a Date: ./app show_entry_cal <date>\n"
        "Help Page: ./app -h"
    )
    print(menu)