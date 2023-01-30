# Chat bot for Elite 101 - Food delivery


def print_welcome():
  print("Welcome to FoodDev")
  print("------------------")


def get_user_name():
  global username
  username = input("Please enter your name: ")
  print("Welcome " + username)


print_welcome()
get_user_name()
