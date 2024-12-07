# Made by Sean "seanAIMS" Campbell
# Twitter: @seanAIMSS
# YouTube: youtube.com/@seanAIMS
# Total AI Generated Lines of Code: 5-10
# V1 Finished in 1h 37m
# V2 ()
# ----------------------------------
# Additional Ideas: 
# 1 - Add a function which allows users to search for mice based on weight.

import time

# Main Mouse Class For Data Insertion. | Functional - 12/7/24
class Mouse:
    def __init__(self, name, weight):
        self.name = name 
        self.weight = weight
        
    def __str__(self):
        return f"\033[1m{self.name}\033[0m -- {self.weight}"

# Making Empty List for Other Mice to Be Inputted. | Functional - 12/7/24
mouseCollection = []

# Initial prompts to see the collection list or add mice to the list. | Functional - 12/7/24
time.sleep(2)
print("Initializing...")
time.sleep(3)
print("Initialized.")
time.sleep(2)
print("")

# Main loop to continuously wait for user input. | Functional - 12/7/24
while True:
    initialBootQuestion = input("\033[1mHello!\033[0m Are you here to check inventory, add to the list, or quit? | :> ")
    if "add" in initialBootQuestion:
        try:
            newMice = int(input("How many mice would you like to add? | :> "))
            for i in range(newMice):
                print(f"Adding mouse {i + 1} of {newMice}...")
                mouseNameInput = input("Kindly, add the name of the mouse! | :> ")
                mouseWeightInput = input("Okay, now the weight? | :> ")
                mouse = Mouse(mouseNameInput, mouseWeightInput)
                mouseCollection.append(str(mouse))
            print("\nAll mice added! Here's the updated inventory:")
            print("\n".join(mouseCollection))
        except ValueError:
            print("Hm. That wasn't a valid number. Please try again.")

    # Exit the program. | Functional - 12/7/24
    elif "quit" in initialBootQuestion:
        print("Exiting program...")
        break  # Exit the while loop to terminate the program.

    # Check current inventory. | Functional - 12/7/24
    elif "check" in initialBootQuestion:
        print("Okay, here's what is currently in inventory!")
        print("\n".join(mouseCollection) if mouseCollection else "No mice in inventory.")

    # Retry logic for invalid input. | Functional - 12/7/24
    else:
        retry = input("Something went wrong. Type 'add', 'check', or 'quit' | :> ")
        if "add" in retry:
            try:
                newMice = int(input("How many mice would you like to add? | :> "))
                for i in range(newMice):
                    print(f"Adding mouse {i + 1} of {newMice}...")
                    mouseNameInput = input("Kindly, add the name of the mouse! | :> ")
                    mouseWeightInput = input("Okay, now the weight? | :> ")
                    mouse = Mouse(mouseNameInput, mouseWeightInput)
                    mouseCollection.append(str(mouse))
                print("\nAll mice added! Here's the updated inventory:")
                print("\n".join(mouseCollection))
            except ValueError:
                print("Hm. That wasn't a valid number. Please try again.")
        elif "quit" in retry:
            print("Exiting program...")
            break  
        elif "check" in retry:
            print("Okay, here's what is currently in inventory!")
            print("\n".join(mouseCollection) if mouseCollection else "No mice in inventory.")
        else:
            print("Hm...odd. Shutting down...")
            break 

# Class Testing | Functional - 12/7/24
# Uncomment this section to test creating and printing a single mouse instance.
# mouse1 = Mouse("Pulsar X2H Mini", 52)
# print(f"{mouse1}")  # Outputs: Pulsar X2H Mini - 52
