import random
# Winning Rules of the Rock paper scissor game as follows:
# Rock vs paper->paper wins
# Rock vs scissor->Rock wins
# paper vs scissor->scissor wins
print("Hey! Enter your name ")

name =input(str())
print("Hi"+" "+ name )
while True:
 print("\nEnter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n ")
 user_choice = int(input("User turn, type your choice(number):  "))

 while user_choice > 3 or user_choice < 1:
     user_choice =  int(input("Please enter valid input " +" "+name+":  "))
 if user_choice == 1 :
     choice_name = 'Rock'
 elif user_choice == 2 :
     choice_name = 'Paper'
 else :
     choice_name = 'Scissor'
 print(name+"\nYour choice is :" + choice_name +" \nNow its computer turn....... ")

 comp_choice = random.randint(1,3)
 while comp_choice == user_choice :
     comp_choice = random.randint(1, 3)

 if comp_choice == 1:
     comp_choice_name = 'Rock'
 elif comp_choice == 2:
     comp_choice_name = 'Paper'
 else:
     comp_choice_name = 'Scissor'
 print("Computer choice is: " + comp_choice_name +
  "\n"+ choice_name + " V/s " + comp_choice_name)

 if ((user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice ==1)) :
    print("Paper wins => ", end="")
    result ="Paper"
 elif((user_choice== 1 and comp_choice == 3) or (user_choice== 3 and comp_choice == 1)) :
    print("Rock wins =>", end="")
    result ="Rock"
 elif((user_choice== 1 and comp_choice== 1) or (user_choice== 2 and comp_choice== 2) or (user_choice== 3 and comp_choice== 3)):
    print("game draw", end="")
 else :
    print("Scissor wins =>", end="")
    result = "Scissors"

 if result == choice_name :
      print("\n<== "+ name + ' ' +"wins ==>")
 elif user_choice== comp_choice:
     print("no winner")
 else:
      print(" \n<== Computer wins ==>")

 print("Do you want to play again? (Y/N)")
 ans = input()
 if ans == 'n' or ans == 'N':
    break


print("\nThanks for playing" +' '+ name)