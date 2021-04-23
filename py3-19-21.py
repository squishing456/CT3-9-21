import random
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
#Above, you can see some text! the "def mainProgram" function defines EVERYTHING you see below.
#Below, you can see we show the user their different options to pick from.
#Each of these options refer to a function.
            
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""
    O~~LIST MANIA~~O

    1. Add to a list, or
    2. Return the value at an index
    3. Add a bunch of numbers
    4. Print contents of list
    5. Sort Your List

    ---------------------
    |~~MARKSMAN SEARCH~~|
       "We Never Miss!"
    ---------------------
    
    6. Random search
    7. Linear Search
    8. Recursive Binary Search
    9. Iterative Binary Search
    10. Exit program""")

#Here is where we call our function. This basically connects the user's input (desired funciton) to the function itself.
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                addABunch()
            elif choice == "4":
                printLists()
            elif choice == "6":
                randomSearch()
            elif choice == "7":
                linearSearch()
            elif choice == "8":
                binSearch = input("What are you looking for?")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "9":
                searchItem = input("What are you looking for?")
                result = iterativeBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
            elif choice == "5":
                sortList(myList)
            else:
                break
        except:
            print("You caught an error. Despicable.")
#In the four lines above, you can see what happens when the user messes up.
#If they enter a number that's not able to be called, the program will quit.
#If they make another type of error, it will display the message.
#Here is where the functions are actually defined.

            
def addToList():
	print("Adding to a list! Great choice!")
	newItem = input ("Type an integer here!  ")
	myList.append(newItem) 
	myList.append(newItem)

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?")
    numRange = input ("And how high would you like these numbers to go?")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    print("rAnDoM sEaRcH")
    print(myList[random.randint(0, len(myList)-1)])
    

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?  ")
    print(myList[int(indexPos)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("What you lookin for, partner?")
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_liste, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("You ding dang found it at index position {}".format(mid))
            return mid
        
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high =len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted? ")
        if whichOne.lower() == "sorted":
                print(unique_list)
    
    


#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
	mainProgram()
