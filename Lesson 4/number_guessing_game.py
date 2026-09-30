#Number Guessing Game
secret_num = 31
number = int(input("WELCOME TO THE GUESSING GAME! ENTER A NUMBER TO START GUESSING THE NUMBER!:"))
if number == 31:
    print("Genius, you have guessed the right number. GOOD JOB")
    print("End of the game!")
    print("=====================================================================================")
else:
 print("Not the number, good try, four guesses left!")

number = int(input("THIS IS YOUR SECOND TRY, ENTER YOUR NUMBER:"))
if number == 31: 
 print("Excellent, you have guessed the right number in two tries. GOOD JOB")
 print("=====================================================================================")
else:
 print("Not the number, good try, three guesses left!")

number = int(input(" THIS IS YOUR THIRD TRY! ENTER YOUR GUESSED NUMBER:"))
print("=====================================================================================")
if number == 31:
 print("You got it right. Good job")
else:
  print("Not the right number, you have two tries left!")

number = int(input("THIS IS YOUR FOURTH TRY, ENTER YOUR NUMBER:"))
if number == 31:
 print("Excellent, you have guessed the right number in four tries. GOOD JOB")
 print("=====================================================================================")
else:
 print("Not the number, good try, one guess left!")
    

 number = int(input("THIS IS YOUR LAST TRY, ENTER YOUR NUMBER:"))
if number == 31:  
 print("You have guessed the right number in four tries. you'll get it next time!, Answer was 31")
else:
 print("SORRY YOU HAVE FAILED THE GAME! ")







