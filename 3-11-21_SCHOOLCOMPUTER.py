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
    2. Return the value at an index
    3. Exit program""")
            if choice == "1":
                    addToList()
            elif choice == "2":
                    indexValues()
                    break
	#TO ADD(what to add)" 1. a way to loop the action, 2. A way to quit. 3. Think of repitition

def addToList():
	print("Adding to a list! Great choice!")
	newItem = input ("Type an integer here!  ")
	myList.append(newItem) 

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    input("What index position are you curious about?  ")
    print(myList[int(indexPos)])

#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
	mainProgram()
