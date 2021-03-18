"""
Program goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
	a. Add more values to a list
	b. Return a value to a specific index
"""

myList = []
def mainProgram():
            while True:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input ("""1. Add to a list, or
    2. Add a bunch of numbers
    3. Return the value at an index
    4. Random search
    5. Print contents of list
    6. Exit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "5"
                
                
                    break
	#TO ADD(what to add)" 1. a way to loop the action, 2. A way to quit. 3. Think of repitition

def addToList():
	print("Adding to a list! Great choice!")
	newItem = input ("Type an integer here!  ")
	myList.append(newItem)

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?")
    numRange = input ("And how high would you like these numbers to go?")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def randomSearch

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

            
#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
	mainProgram()
