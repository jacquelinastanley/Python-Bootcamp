#Create a simle quiz program with 3 questions. At the end of the quiz, disply score. 

score = 0
print("Welcome to the quiz! Please answer the following questions:")

#Question 1
answer1 = input("What is 2 + 5? ")
if answer1 == "7":
    print("Correct!")
    score += 1
    print (f" Your current score is: {score}")
else:
    print("Incorrect. The correct answer is 7.")

#Question 2
answer2 = input("What is 5 + 7? ")
if answer2 == "12":
    print("Correct!")
    score += 1
    print (f" Your current score is: {score}")
else:
    print("Incorrect. The correct answer is 12.")   


#Question 3
answer3 = input("What is 7 + 7? ")
if answer3 == "14":
    print("Correct!")       
    score += 1
    print (f" Your current score is: {score}")
else:
    print("Incorrect. The correct answer is 14.")


#Final Score 
print (f"Your final score is: {score} out of 3.")
if score == 3:
    print("Excellent! You got all the answers correct!")    
elif score == 2:
    print("Good job! You got 2 out of 3 correct.")
elif score == 1:
    print("You got 1 out of 3 correct. Keep practicing!")
else:
    print("Don't worry, you can try again and improve your score!")


