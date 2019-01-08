#LISTS
#To save a list of variables.
#Say a list of strings to store names of subjects:
subjects = ['History' , 'Physics' , 'Maths' , 'Accounts']

#Length of a list can be found by len() function that takes the list's name as the argument
print(len(subjects))
print()

#To access the ith element of list subjects : subjects[i]
print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[3])
print()
#For C++ and JAVA the range of index given to the list lies between 0 and n-1.
#While in Python we can also give negetive index:
#To access the last element we use -1.
print(subjects[-1]) #Last element
print(subjects[-2]) #Second last
print(subjects[-3]) #Third Last
print(subjects[-4]) #Forth last or 0th element in this case.
print()

#SLICING
#We can also access a range of values at index between range i to j (including i and excluding j)
print(subjects[0:2])
print(subjects[1:]) #Assumes j = length of list , if not metioned
print(subjects[:3]) #Assumes i = 0 , if not mentioned
print()

#TO ADD AN ITEM TO THE LIST
#Use append() method to add an item at the end position.
subjects.append("Chemistry")
print(subjects[0:])
print()
#To insert at a specific location : insert() method
#insert() takes 2 arrguments : 1.Location 2.Value to be inserted
subjects.insert(2 , "Geography")
print(subjects) #We can print the complete List by just giving its Name to the print function.
print()
#We can also use insert to insert another list in a list:
fruits = ["Apple" , "Banana" , "Mango"]
fruits2 = ["Kiwi" , "Orange"]
fruits.insert(1 , fruits2)
print(fruits)
print(fruits[1])
print()
