import random
myList = []
unique_list = []

  print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input ("""1. Add to a list, or
    2. Return the value at an index
    3. Exit program
    2. Add a bunch of numbers
    3. Return the value at an index
    4. Random search
    5. Linear Search
    6. Recursive Binary Search
    7. Iterative Binary Search
    8. Print contents of list
    9. Exit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                addABunch()
            elif choice == "4"
                randomSearch()
            elif choice == "5"
                linearSearch()
            elif choice == "6"
                searchItem = input("What are you looking for?")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem)
            elif choice == "7"
                searchItem = input("What are you looking for?")
                result = iterativeBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem)
                                      
            elif choice == "8"
                print(myList)
            else:
                break
        except:
            print("You caught an error!")
	#TO ADD(what to add)" 1. a way to loop the action, 2. A way to quit. 3. Think of repitition

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
    if showMe.lower() == "y"
        pring(unique_list)

def randomSearch
    print("rAnDoM sEaRcH")
    print(myList[random.randint(0, len(myList)-1)])
    

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    input("What index position are you curious about?  ")
    print(myList[int(indexPos)])

def linearSearch
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("What you lookin for, partner?")
    for x in range (len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high+low) // 2

        if unique_list[mid] == x:
            print("You ding dang found it t index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1 x)
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
    
    


#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
	mainProgram()
