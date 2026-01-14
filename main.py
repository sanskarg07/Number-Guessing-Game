import random
import time
print("✨🔰 Welcome to the Game 🔰✨")
print('''📝Instructions for game :-
    🪶 Computer will choose a number and you have to guess it.
    🪶 If you'll guess wrong number it'll inform you.
        -> You are high = guess lower number.
        -> You are low = guess higher number.
    🪶 Type "end" to quit the game anytime.
      ''')

def game():
    computer = random.randrange(100)
    round_no = 1
    TIME_LIMIT = 40
    start_time = time.time()
    print(f"You have {TIME_LIMIT} seconds to guess right number💭")
    print("Guess the number between 1 to 100 📈")
    print("\n")

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = int(TIME_LIMIT - elapsed_time)
        if remaining_time <= 0:
            print("⏰Time's up  ! Better luck next time...")
            print(f"The number was : {computer}")
            break
    
        else:
            print(f"Round : {round_no}")
            print(f"You have {remaining_time} seconds left to guess 📈")
            user = (input("What is your guess 🤔💭 : "))
            if user == "end" :
                break

            try:
                user = int(user)
                if user == computer:
                    print (f"Congrats🎉! You won in {round_no} Rounds! ")
                    print(f"You made it in {round_no} rounds 😁❤️")
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

def replay():
    confirm = input("Press Enter to start : ")
    if confirm == None or True:
        game()
        another = input("Do you wanna play it again 😊? (yes/no) : ")
        if another!= "yes":
            for i in range (2):
                print("Please 😣")
                another = input("What you say : ")
                if another.lower() in ["yes","ok","okay"]:
                    print("\n")
                    print("Thanks for playing it again!😊")
                    game()
                    break           
        elif another in ["yes","Yes"] :
            print("\n")
            game()
    

while True:
    replay()
    print("Thanks for playing ❤️")
    break