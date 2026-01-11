import random
def game():
    computer = random.randrange(100)
    round_no = 1
    print("Welcome to the Game 🔰✨")
    print("Guess the number between 1 to 100 📈")
    while True:
        print(f"Round : {round_no}")
        user = (input("What is your guess 🤔💭 : "))
        if user == "end" :
            break

        try:
            user = int(user)
            if user == computer:
                print (f"Congrats🎉! You won in {round_no} Rounds! ")
                round_no +=1
                break

            elif (user>computer):
                print("You are high 😅! Give it another try😉\n")
                round_no +=1
        
            elif (user<computer):
                print("You are low 😅! Give it another try😉\n")
                round_no +=1

        except ValueError:
            print("Error ⚠️! You Entered a wrong value!\n")
            continue
            

        print(f"You made it in {round_no} rounds 😁❤️")

while True:
    game()
    another = input("Do you wanna play it again 😊? (yes/no) : ")
    if another!= "yes":
        for i in range (3):
            print("Please 😣")
            another = input("What you say : ")
            if another == "yes":
                game()
                break           
    break

print("Thanks for playing ❤️")