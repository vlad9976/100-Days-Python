print(r"""          ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
               Welcome To Treasure hunt game! :) 
               Type 'start' To start the game
""")

start = input("Type Start > ").lower()

if start == "start":
    first_choice = input("Where Would you like to go? Type left OR right:\n> ").lower()
    if first_choice == "right":
        print("Sorry, you fell into a hole\nGame Over!")
    elif first_choice == "left":
        lake = input("You came to a lake What would you do:\nType wait(To wait for a boat) OR swim(To swin across the lake \n>  ").lower()
        if lake == "swim":
            print("Sorry, you got eaten by some monster HAHA\nGame Over!")
        elif lake == "wait":
            print("The boat arrived and you got across the lake")
            choose_door = input("You came to castle with 3 doors: Type red,green,blue To choose a door\nChoose a Door \n>").lower()
            if choose_door == "red":
                print("the RED room is on fire!\nGame Over!")
            elif choose_door == "blue":
                print("Sorry, the room i flooded\nGame Over!")
            elif choose_door == "green":
                print("Great you found the Treasure :)\nThank you playing ")
                print(r'''              |                   |                  |                     |
                 _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                          |                `"=._o`"=._      _`"=._                     |
                 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/
                ''')
            else:
                print("No such Room! Game Over")
        else:
            print("No such direction! Game over")
    else:
        print("No such choice! Game over")
else:
    print("Incorrect Please type start! Next time, Game over")