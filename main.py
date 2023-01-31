# Chat bot for Elite 101 - Food delivery


def print_welcome():
  print("Welcome to FoodDev")
  print("------------------")


def get_user_name():
  global username
  username = input("Please enter your name: ")
  print("Welcome " + username)


def search_restaurant_by_name():
  print("TODO: Search restaurant by name")


def search_restaurant_by_type():
  print("TODO: Search restaurant by type")


def user_preferences():
  print("TODO: User preferences")


def main_menu():
  while True:
    print("[1] Search restaurant by name")
    print("[2] Select restaurant by food type")
    print("[3] User preferences")
    print("[Q] Quit")
    user_input = input("Select an option: ").upper()

    if user_input == '1':
      search_restaurant_by_name()
    if user_input == '2':
      search_restaurant_by_type()
    if user_input == '3':
      user_preferences()
    if user_input == 'Q':
      break
    print("")


print_welcome()
get_user_name()
main_menu()
