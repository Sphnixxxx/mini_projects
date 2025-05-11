import random
items=["rock","paper","scissor"]
user_choice=input("enter your choice(rock,paper,scissor): ")
comp_choice=random.choice(items)
print(f"user choice = {user_choice} \ncomputer choice= {comp_choice}")
if user_choice == comp_choice:
    print("Tie !!!")
elif user_choice =="rock":
    if comp_choice == "paper":
        print("paper covers:computer  win")
    else:
        print("rock : you win")
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor : computer win")
    else:
        print("paper: user win")
else:
    if comp_choice=="rock":
        print("rock:computer win")
    else:
        print("scissor : you win")


