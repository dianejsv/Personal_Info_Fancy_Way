# Importing necessary modules
import pyfiglet
from colorama import Fore
import time

# Asking for the user input
# Prompt the user to enter name
name = input("Enter your name: ")
# Prompt the user to enter age
age = input("Enter your age: ")
# Prompt the user to enter dream job
dream_job = input("What's your dream job? ")
# Prompt the user to enter contact number
contact_number = input("Enter your Contact Number: ")
# Prompt the user to enter the city
city_you_live_in = input("Enter the City you live in: ")

# Generating fancy ASCII art for user's information
fancy_text_name = pyfiglet.figlet_format(name, font="doom")
fancy_text_age = pyfiglet.figlet_format(age, font="doom")
fancy_text_dream_job = pyfiglet.figlet_format(dream_job, font="starwars")
fancy_text_contact_number = pyfiglet.figlet_format(contact_number, font="starwars")
fancy_text_city_you_live_in = pyfiglet.figlet_format(city_you_live_in, font="starwars")

# Applying color to the generated ASCII art text
colored_fancy_name = Fore.LIGHTCYAN_EX + fancy_text_name + Fore.RESET
colored_fancy_age = Fore.MAGENTA + fancy_text_age + Fore.RESET
colored_fancy_dream_job = Fore.LIGHTCYAN_EX + fancy_text_dream_job + Fore.RESET
colored_fancy_contact_number = Fore.LIGHTMAGENTA_EX + fancy_text_contact_number + Fore.RESET
colored_city_you_live_in = Fore.LIGHTCYAN_EX + fancy_text_city_you_live_in + Fore.RESET

# Printing user's information together with ASCII art and color
print("Your Information:")
print("Name: ", end='')
for char in colored_fancy_name:
    print(char, end='', flush=True)
    time.sleep(0.01)
print("\nAge: ", end='')
for char in colored_fancy_age:
    print(char, end='', flush=True)
    time.sleep(0.01)
print("\nDream Job: ", end='')
for char in colored_fancy_dream_job:
    print(char, end='', flush=True)
    time.sleep(0.01)
print("\nContact Number: ", end='')
for char in colored_fancy_contact_number:
    print(char, end='', flush=True)
    time.sleep(0.01)
print("\nCity: ", end='')
for char in colored_city_you_live_in:
    print(char, end='', flush=True)
    time.sleep(0.01)
# Printing thank you message
