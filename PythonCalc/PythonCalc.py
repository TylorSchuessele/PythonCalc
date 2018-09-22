

def bubbleSort(numL = []):
    average = 0.0
    for j in range (len(numL) -1):
        for i in range (len(numL) - 1 - j):
            if(numL[i] > numL[i+1]):
               temp = numL[i]
               numL[i] = numL[i+1]
               numL[i+1] = temp
         
    return numL

def listIn():
    num= ""
    numList = []
    while num != "end":
        num = input()
        try:
            numList.append(float(num))
        except:
            if num != "end":
                print("Invalid Number")
    return numList

def meanmedianmode():
    print("Enter The Numbers")
    #Obtains list by calling listIn Function
    numList = listIn() 
    #passes List to average Function
    avg = average(numList) 
    #prints the mean / Average
    print ("The Mean is " +  str(avg))
    # sorts List so that median can be found
    numList = bubbleSort(numList) 
    # Even amount of numbers in List Takes the 2 middle numbers of the sorted List and Gets Average 
    if len(numList) % 2 == 0: 
        median = (numList[len(numList)/2] + numList[len(numList)/2 + 1] ) / 2 
    else: # Odd amount of Numbers in List takes the middle value of List by dividing in half and rounding up
        median = numList[ int(len(numList)/2)] 
    # Prints out median 
    print ("The Median is " + str(median)) 

def average(numL = []):
    average = 0.0
    for i in numL:
        average = average + i
    try:
        average = average / len(numL)
    except ZeroDivisionError:
        print("Please Enter atleast 1 number")
    return average

def standardDiviation():
    print("Enter the numbers you want the standard diviation of")
    numList = listIn()
    avg = average(numList)
    sDiv = 0.0
    for i in numList:
        sDiv = sDiv + (i - avg)**2
    sDiv = sDiv / ( len(numList) -1 )   
    print ("The Standard Diviation is " + str(sDiv))

def simpleMath():
    print("Do Math")
    equation = input()
    equation = equation.replace("x","*")
    equation = equation.replace("^","**")

    if(equation == "stDiv" or equation == "sDiv" or equation == "stdiv" or equation == "sdiv"):
        standardDiviation()
    elif(equation =="average" or equation == "avg" or equation == "mean" or equation == "mode" or equation == "median"):
        meanmedianmode()
    else:
        try:
            answer = eval(equation)
            print (answer)
        except SyntaxError:
            print ("invalid math equation use + - * / symbols")
        except ZeroDivisionError:
            print("Error cannot do 0/0")
        except:
            print("Error, Please Try Again")
        





def start():
    while True:
        simpleMath()

start()

