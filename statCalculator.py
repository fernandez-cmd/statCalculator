#Jovani Fernandez
#Project_1
#csi_31
#DO2[31095]

data = []
#Function Below used to aquire user input
def userInputFun():
    finishinput = False

    while finishinput == False:
        userinput=input("Enter a number to your data or 0 to finish:")

        #Code below checks to see if user if user is finished entering data
        if userinput == "0":
            print(data)
            finishinput = True

        #Code below checks to see if input was valid in this case we need numbers   
        elif userinput.isdigit() == False:


            #Code below handles error when user enter a value besides a number 
            try:
                data.append(int(userinput))
            except:
                data.append(int(input("PLEASE USE NUMERIC VALUES")))
            
        #Code below appends the datas list with proper data type
        else:
            data.append(int(userinput))

userInputFun()

#code below sorts the dats set given by the user. and is globally stored.
sortedData=sorted(data)



def minOf(dataset):
    minimum = sortedData[0]
    print ("min =" , minimum)
minOf(sortedData)

def maxOf(dataset):
    maximum = sortedData[-1]
    print ("max =" , maximum)
maxOf(sortedData)


#Below is the function that will caculate the mode of the data set.
def modeof(dataset): 
    #Below I import counter from the collections module

    from collections import Counter


    #List below is initialized to store the value of values of mode
    mode=[]

    #Line below creates a dict. of the data set 
    c=Counter(sortedData)

    maxcount = max(c.values())
    for num, c in c.items():
        if c == maxcount:

            #Line below appends our mode[] for the final solution 
            mode.append(num)
    print ("mode=", mode)
            



modeof(sortedData)

#Below is the function that will caculate the median of the data set.
def med(dataset):

    #This will help determine if the length of list is even or odd
    #Line below is vital, variable is locally stored.

    dataMod=(len(sortedData)%2)

    #Conditional below hold two possible outcomes if the list length is
    #Even an additional step is required for the desired output
    
    if(dataMod == 0):
        #variable below stores the INDEX of the value and NOT THE VALUE! 
        indexEven1 = (int(len(sortedData)//2) - 1)
        indexEven2 = (int(len(sortedData)//2))


        #Variable below grabs the value at the index needed
        #and performs the simple operation to aquire the median  
        median = (sortedData[indexEven1] + sortedData[indexEven2])/2
        print("med =" , median)
        
    #there are only 2 possible outcomes. Either the list length is even or odd,
    #for that reason we dont need any other conditonal statements 
    else:
        indexOdd=len(sortedData)//2
        median = sortedData[indexOdd]
        
        print("med =" , median )



med(sortedData)


#Below is the function that will caculate the mean of the data set.
def mean(dataset):

    #Variable below aquires the length
    #required to find the mean or the usual average
    lengthOfData= len(data)

    #Variable below stores the sum of the data
    #required to find the mean or the usual average
    sumOfData = 0


    #For-loop belows iterates through each element of the data set and
    #performs the addition operation and stores the total to sumOfData
    for num in data:
        sumOfData += num

    #variable below stores and perform the final division operation to determine the mean or usual average
    solutionForMean = sumOfData / lengthOfData
    print("mean=",solutionForMean)
   


mean(sortedData)












