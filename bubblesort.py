def funcSorter(userInput):
  counter = 0
  for i in range(len(userInput)):
    for j in range(0,len(userInput)-i-1):
      if int(userInput[j]) > int(userInput[j+1]):
        standIn = int(userInput[j])
        userInput[j] = int(userInput[j+1])
        userInput[j+1] = standIn   
        counter += 1
  return counter
userNum = input("Please enter values needed to be sorted here seperated by commas: \n")
userNum = userNum.split(",")
swapCounter = funcSorter(userNum)
print("Sorted List:", userNum, "\n", "The number of swaps are:", swapCounter)