Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.


Input:  2 Name y

Expected Output:

2

Name

y

ANSWER

# Taking input from the user
num = int(input())       # Read an integer
text = input()           # Read a string
ch = input()             # Read a character

# Output each input on a new line
print(num)
print(text)
print(ch)


Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.

If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.

Input: 45 45 45

Expected Output: 

Triangle cannot be formed

Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output.

ANSWER

  # Read three angle values from the user
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# Calculate the sum of the angles
sum_of_angles = angle1 + angle2 + angle3

# Check if the triangle can be formed
if sum_of_angles == 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")



Prob 3: 

Given mark of student, Print the Grade

Grade A if mark is greater than or equal to 90

Grade B if mark is greater than or equal to 80

Grade C if mark if greater than or equal to 60

Grade D if mark if greaer than or equal to 35

Fail if mark is lesser than 35


Input: 95

Expected Output:

Grade A

Explanation: Here 95 is greater than or equal to 90 so its Grade A

ANSWER

# Read the student's mark
mark = int(input())

# Determine the grade based on the mark
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 35:
    print("Grade D")
else:
    print("Fail")


Prob 4: Write a program using switch case which takes a value and prints the respective Size.
If size is 29 then its small

If size is 30 then its Medium

If size is 38 then its Large

If size is 42 then its XLarge

If size is not any of the above then Invalid.



Input: 29

Expected Output: 

Small


ANSWER
  
# Read the size value from the user
size = int(input())

# Match-case structure to check size
match size:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("XLarge")
    case _:
        print("Invalid")
alternate method

size = int(input())

if size == 29:
    print("Small")
elif size == 30:
    print("Medium")
elif size == 38:
    print("Large")
elif size == 42:
    print("XLarge")
else:
    print("Invalid")
