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

#CREATING LIST USNG LOOP:
#Use the element to to entered with the for loop to iterate
listByLoop = [0 for i in range(0,10)]
print(listByLoop)
listByLoop2 = [i for i in range(0,10)]
print(listByLoop2)
stringForLooping = "Hello"
listByLoop3 = [i for i in stringForLooping]
print(listByLoop3)
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
#Now if want all the values of a list to be appened in another list : extend() method
fruits.extend(fruits2)
print(fruits)
print()

#REMOVE VALUE
#To remove a value : remove() method.
print(subjects)
subjects.remove("Geography")
print(subjects)
#Use pop() method to remove the last value of the list.
subjects.pop()
print(subjects)
print()

#REVERSING A LIST : reverse() method.
subjects.reverse()
print(subjects)
print()

#SORTING
#In Dictionary order : sort() method (for a string type list)
subjects.sort()
print(subjects)
print()
#Sort method when applied to a list of numbers : sorts in asscending order.
numbers = [3,7,2,8,9,1,0]
numbers.sort()
print(numbers)
#To sort a number list in decending order : pass a reverse arrgument.
numbers.sort(reverse = True)
print(numbers)
print()
subjects.sort(reverse = True)
print(subjects)
#Here sort() method does the sorting inplace (Does not return anything).
#But if we don't want inplace : sorted() function : Arrgument->ListName
subjects2=sorted(subjects)
print(subjects2)
print()

#SIMPLE OPERATIONS ON A NUMBERS LIST:
#min() and max() to get minimum and maximum number.
#min() and max() also works for a list of strings.
#sum() to get the sum of all numbers of the list (Error for list of string)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()
print(min(subjects)) #Minmum as dictionary order.
print(max(subjects)) #Maximum as dictionary order.
print()

#SEARCHING
#To find the index of a certain value in out list : index() method.
#But this gives an error if the value does not exits in the list.
print(subjects)
print(subjects.index("History"))
#To avoid the error : we need to check wheather the value exits in the list or not.
#To do this we use a simple command : Value in listName : This returns a boolean value.
print("Music" in subjects)
print("Maths" in subjects)
print()

#Now to Iterate to all values of a list : use a for LOOP :
for i in subjects:
    print(i)
print() #Not a part of for loop (read below for explaination)
#Here we use i as an iterator (Not defined before but can be used in this way).
#So using i we access all the values of the list.
#Also here important point to be noted is we use indentation
#We do not need to put {} these brackets in Python
#All the code that is under the for loop statment with a <tab> is a part of the loop.

#Now if want the values as well as the we use enumerate() function
#enumerate() function takes list name as a parameter and returns index and values:
#So for 2 values returned we have to take 2 variables.
for i,a in enumerate(subjects):
    print(i,a)
print()
#Also we can pass another argument to set the starting index of the numbering:
for i,a in enumerate(subjects , start = 1):
    print(i,a)
print()

#GETTING STRING VERSION OF A COMPLETE LIST OF STRINGS:
#Use the join() method it is used on a string that is used as a token.
#Syntax : "Token".join(ListName) : Returns a string.
subjectsSrting = ", ".join(subjects)
print(subjectsSrting)

#MAKING LIST USING A STRING:
#Use split() method to form a list using a string.
#It is used on a string and returns a list.
#Takes an argument : the sub-string about which we have to split the string.
sampleString = "Apple . Orange . Mango . Banana"
print(sampleString)
sampleList = sampleString.split(" . ");
print(sampleList);
print()

#COPYING A LIST TO ANOTHER:
subjects2 = subjects
#Now Any change made in the orignal list are reflected in the copied list.
subjects[0] = "Economics"
print(subjects)
print(subjects2)
print()



#TUPLES
#They are similar to lists , only one differnce:
#There values once assinged can't be changed : Immutable.
sampleTuple = (1,5,7,3,8,9)
print("Tuple:")
print(sampleTuple)
print()



#SETS
#They are unordered and have no duplicates.
#Also {} these are used to initialise them.
mobileBrands = {"Samsung" , "Nokia" , "Apple" , "MI"}
print("Set:")
print(mobileBrands)
#Now on running this code mupliple times we get outputs in differenet order (unorded).
#Use of Sets:
#This statment returns true or false : maths in subjects
#This can be done on all lists , tuples and sets. But it is very efficent in sets.
print("MI" in mobileBrands)

#INTERSECTION , UNION AND DIFFERENCE
#To find out what is common in the 2 sets : intersection() method.
mobileBrands2 = {"OnePlus" , "MI" , "Honor" , "Apple"}
print(mobileBrands.intersection(mobileBrands2))
#Now for set1 - set2 : set1.difference(set2)
print(mobileBrands.difference(mobileBrands2))
print(mobileBrands2.difference(mobileBrands))
#For union : union() method
print(mobileBrands.union(mobileBrands2))
print()


#CREATING EMPTY LISTS , TUPLES AND SETS:

#Empty list:
emptyList = []
emptyList2 = list() #list Class

#Empty Tuples:
emptyTuples = ()
emptyTuples2 = tuple() #tuple class

#Empty Set:
emptySet = {} #WRONG : This creates an empty dictionary : Discussed later.
emptySet2 = set() #Right : using set class.
