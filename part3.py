'''
***PART 4***

In the program below, the user is repeatedly prompted to enter integers until they enter 0. Afterward, the program is supposed to take the average of the nonzero numbers entered, but the program is incomplete. Fix the code below so that the average of the nonzero numbers is found and printed in the indicated sentence.

(Hint: this may require a new variable declared before the while loop that keeps track of how many numbers have been input/added already)

Example of what should appear on console when this part runs:

Enter a number or enter 0 to stop: 5
Enter a number or enter 0 to stop: 6
Enter a number or enter 0 to stop: 7
Enter a number or enter 0 to stop: 0
Average: 6.0

'''
num = int(input("Enter a number or enter 0 to stop:"))
total = 0

while num != 0:
  total = total + num
  num = int(input("Enter a number or enter 0 to stop:"))
    
print("Average:", total)
