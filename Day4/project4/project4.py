# Rock Paper Scissors
import random

choises=["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\nRock""",
"""
      _______
 ---'    ____)____
            ______)
           _______)
          _______)
 ---.__________)
\nPaper""",

 """
     _______
 ---'   ____)____
           ______)
        __________)
       (____)
 ---.__(___)
 \nScissors"""
         ]
print("Hello to Rock Paper Scissors Game :)\nChoose 0 for Rock, 1 For Paper and 2 for Scissors")


my_pick=int(input("Please pick:\n> "))

index_comp=random.randint(0,2)
print(index_comp)
computer_pick=choises[index_comp]

if my_pick == 0 and index_comp == 0:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[0]}\nDraw")
elif my_pick == 0 and index_comp == 1:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[1]}\nSorry you Lost")
elif my_pick == 1 and index_comp == 1:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[2]}\nDraw")
elif my_pick == 1 and index_comp == 2:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[2]}\nSorry you Lost")
elif my_pick == 2 and index_comp == 2:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[2]}\nDraw")
elif my_pick == 2 and index_comp == 0:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[0]}\nSorry you Lost")
else:
    print(f"you chose {choises[my_pick]}\nThe computer chose {choises[index_comp]}\nYou Won!")