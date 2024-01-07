print("============================================================= \n")
print("ASSIGNMENT BY: SULAIMAN SHAMS \nSUBMITTED TO: Sir, SYED SHAKAIB \n")
print("=============================================================")

print("\nQUESTION 1. \nQUESTION 2.\nQUESTION 3.\nQUESTION 4. \nQUESTION 5.\nQUESTION 6. \n\n **ENTER QUESTION NUMBER FROM ABOVE TO GET SOLUTION**")

while(True):
    
  x = int(input("\nENTER Q#:"))

  if (x==1):
    a = int(input("ENTER FIRST NUMBER:"))
    b = int(input("ENTER SECOND NUMBER:"))
    sum = a+b
    print(f"The sum of {a} and {b} is {sum}") 

  elif (x==2):
    length = 25
    width = 25
    perimeter = 2*(length+width)
    print(f"The perimeter of the rectangle is {perimeter}")
  elif (x==3):
    email_1 = "sulaimanshams26@gmail.com"
    print(email_1) 

  elif(x==4):
    user_Name00 = 300
    print("USER SCORE IS "+str(user_Name00))

  elif(x==5):
    value_1 = int(input("ENTER VALUE 1: "))
    value_2 = int(input("ENTER VALUE 2: "))
    sum = value_1 + value_2
    multiply = value_2 * value_2
    subtract = value_1 - value_2
    print(f" SUM: {sum} MUL: {multiply} SUB: {subtract}")
  
  elif(x==6):
    input_1 = int(input("Enter value"))
    string_Input = str(input_1)
    print(f"This is my integer variable {string_Input} and i have converted this into string")