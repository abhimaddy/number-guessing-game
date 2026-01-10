import random

computer = random.randint(1,100)
count = 0
print("!!...Welcome To Number Guessing Game...!!")
print("Guess a number between 1 to 100 ")

while True:
    try:
        user_input = int(input("Enter your guess : "))
        if 1 <= user_input <= 100:
            count+=1
            if user_input==computer:
                print(" 🎉 WOOOHOO...  CORRECT GUESS !!")
                print(f" My number was {computer}")
                break
            elif user_input > computer:
                print(" 📈 Too high! Try again!")
            else:
                print(" 📉 Too low! Try again!")
        else:
            print(" ❌ Please enter a number between 1 to 100 ")
    except ValueError:
        print("❌ Invalid Input. Please enter a number")
        

#score logic
if count == 1:
    score = 100
elif count > 1 and count <= 3:
    score = 80
elif count > 3 and count <= 6:
    score = 60
elif count > 6 and count <= 8:
    score = 40
else:
    score = 20
    
print(f"\n Total attemps : {count} ")
print(f" 🏆 Your score : {score} ")
    