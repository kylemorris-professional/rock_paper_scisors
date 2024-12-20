import random
def main():
    while True: #main game loop
        usr_inp = input("r for rock, p for paper, s for scicors: ")
       #game tie
        computer_choice = bot()
        if usr_inp == computer_choice:
            print(f"{usr_inp}  vs  {computer_choice}")
            print("thats a tie")
        #paper beats rock

        elif usr_inp == "p" and computer_choice == "r":
            print(f"{usr_inp}  vs  {computer_choice}")
            print("you win")
      
        #rock beats scisors
        elif usr_inp == "r" and computer_choice == "s":
            print(f"{usr_inp}  vs  {computer_choice}")
            print("you win")
        
        #scicor beats paper
        elif usr_inp == "s" and computer_choice == "p":
            print(f"{usr_inp}  vs  {computer_choice}")
            print("you win")

        else:
            print(f"{usr_inp}  vs  {computer_choice}")
            print("you lose")

#create the bot
def bot():
    tool = ["r", "p", "s"]
    return random.choice(tool)
main()