'''
***PART 5***

Write a program that repeatedly prompts the user to enter numbers until the user enters 0. The program will then count how many of the nonzero inputs are even, and print the number of even inputs in a sentence.

(Hint: For this part, it's likely that you will have an if block inside a while loop. Pay careful attention to the levels of indentation when that happens.)

Example of what should appear on the console when this part runs:

Enter a number or enter 0 to stop: 1
Enter a number or enter 0 to stop: 2
Enter a number or enter 0 to stop: 5
Enter a number or enter 0 to stop: 6
Enter a number or enter 0 to stop: 9
Enter a number or enter 0 to stop: 10
Enter a number or enter 0 to stop: 7
Enter a number or enter 0 to stop: 0
Number of evens: 3

'''

userInput = int(input("Enter a number or enter 0 to stop: "))
evenCount = 0

def inputRevert():
  global userInput
  userInput = int(input("Enter a number or enter 0 to stop: "))


while(userInput != 0):
  if(userInput % 2 == 0):
    evenCount += 1
    inputRevert()
    
  elif(userInput % 2 != 0):
    inputRevert()

print(evenCount)