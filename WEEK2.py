import sys

print("============================ \n BY: SULAIMAN SHAMS \n============================ \n")

while(True):

    input_x = int(input("ENTER QUESTION NUMBER TO GET SOLUTION:"))
    if (input_x == 0):
        sys.exit()

    #Q1.Write a Python program to create an empty set called type
    elif (input_x == 1):
        my_set = set()
        print(type(my_set))

    #Q2.Given a list into a set called
    elif (input_x == 2):
        list_1 = [1,2,3,4,5,5,4,3,2,1]
        unique_set = set(list_1)
        print(unique_set)

    #Q3.Write a Python program to check if a specific element exists in a set.
    elif (input_x == 3):
        fruits_set = {'apple', 'banana', 'orange', 'grape'}
        result = 'banana' in fruits_set #Can be done using loop or if statement
        print(result)

    #Q4.Write a Python program that performs the following operations using set functions:
    elif (input_x == 4):

        set_x1 = {1, 2, 3, 4, 5}
        set_x2 = {4, 5, 6, 7, 8}
        set_union = set_x1.union(set_x2)
        print("UNION:",set_union)
        set_intersection = set_x1.intersection(set_x2)
        print("INTERSECTION:",set_intersection)
        set_subset = set_x1.issubset(set_x2)
        print(set_subset)
        set_x1.add(6)
        print(set_x1)
        set_x1.remove(2)
        print(set_x1)
        set_x3 = {1, 2, 3,}
        print(set_x3)

     #Q5.
    elif (input_x == 5):
        input1_q5 = int(input("Enter first number:"))
        input2_q5 = int(input("Enter second number:"))
        to_tuple = (input1_q5,input2_q5)
        print(to_tuple)

    #Q6.
    elif (input_x == 6):
        names_list = ['Alice', 'Bob', 'Charlie']
        Ages_list = [25, 30, 35]
        people_list_of_tuples = [(names_list[0],Ages_list[0]), (names_list[1], Ages_list[1]), (names_list[2], Ages_list[2])]
        print(people_list_of_tuples)

    #Q7.
    elif (input_x == 7):
        my_tuple = (10,20,30,40,50,60,70,80,90)
        print(my_tuple[-2])
        print(my_tuple[2:7])
        print(my_tuple[-5::2])
        element_100  = 100 in my_tuple
        print(element_100)
        print(my_tuple.index(60))
        #Through LOOP
        index = 0
        for i in my_tuple:
            if i == 60:
                print(i ,",", index)
            index = index + 1
        print(my_tuple.count(30)) #Can be through loop as well

        reverse_list = list(reversed(my_tuple))
        reverse_tuple = tuple(reverse_list)
        print(reverse_tuple)
        my_list = list(my_tuple)
        print(my_list)
        sorted_tuple = tuple(sorted(my_list))
        print(sorted_tuple)

       #Q8. (CHALLENGING QUESTION)
    elif (input_x == 8):
        set_y1 = {1, 2, 3, 4, 5}
        set_y2 = {4, 5, 6, 7, 8}
        set_union = set_y1.union(set_y2)
        print("UNION:", set_union)
        set_intersection = set_y1.intersection(set_y2)
        print("INTERSECTION:", set_intersection)
        set_not_both = set_y1.symmetric_difference(set_y2)
        print(set_not_both)

    #Q9. SET COMPREHENSION (CHALLENGING QUESTION)
    elif (input_x == 9):
        even_square = {n**2 for n in range(1,10) if n%2 == 0}
        print(even_square)


    #Q10 . TUPLE MANIPULATION (CHALLENGING QUESTION)
    elif (input_x == 10):
        mixed_tuple = (12,13.55,10,'sulaiman',5.55)
        int_tuple = tuple(ints for ints in mixed_tuple if isinstance(ints, int))
        print(int_tuple)
        sorted_float_tuple = tuple(sorted(floats for floats in mixed_tuple if isinstance(floats, float)))
        print(sorted_float_tuple)

















