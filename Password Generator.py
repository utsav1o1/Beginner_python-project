import random
print("Your name please!")
name = str(input())
print("Hi"+' '+name+'. '+"\nThis is password generator"+"\n===================")
chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                      '!', '@', '#', '$', '%', '&', '*', '(', ')']
number = 1
print("Easy =  enter password length '4' " +  "\nMedium = enter password length '8' " + "\nStrong = enter password length '12' ")

length = input("\n"+name+ ' '+ "enter your password length = ")
length = int(length)


for password in range(number):
 password = ' '
 for c in range(length):
  password += random.choice(chars)

 print("\n" + name + ", your password is:" + password +"\n\n " +"Thank you for using it" +' '+ name )