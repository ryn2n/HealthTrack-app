def print_error(message):
    error = (
        "Uh oh! Error found.\n\n" + 
        str(message) + "\n\n" +
        "Go back to Home: ./app"
    )
    return error

def home():
    menu = (
        "Welcome to the App!\n"
        "\n"
        "Add New Weight: ./app add_weight <weight>\n"
        "Show Weight Trends: ./app graph_weight [limit]  *note: optional limit, default is 30\n"
        "Weight Data Directory: ./app dir_weight [--change <filename>]\n"
        "Create New Entry: ./app create_entry_cal [date]\n"
        "Show Entry for a Date: ./app show_entry_cal [date]\n"
        "Edit Entry for a Date: ./app edit_entry_cal [date]\n"
        "Create New Food: ./app create_food <name>\n"
        "List all Foods: ./app list_food\n"
        "Show a Food: ./app show_food <name>\n"
        "Edit a Food: ./app edit_food <name>\n"
        "Delete a Food: ./app delete_food <name>\n"
        "Help Page: ./app -h"
    )
    print(menu)