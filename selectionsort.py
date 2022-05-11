def sortList(numInput):
  for i in range(len(numInput)-1):
    min_ind = i
    for j in range(i + 1, len(numInput)):
      if int(userInput[min_ind]) > int(numInput[j]):
        min_ind = j
    numInput[min_ind],numInput[i]=numInput[i],numInput[min_ind] 
    print(numInput[i], "and", numInput[min_ind], "swap", end = ' ')
    print(numInput)
  return numInput
userInput = input("Please enter a list of numbers you want sorted seperated by commas: \n")
userInput = userInput.split(",")
returner = sortList(userInput)
print("Sorted List: ", returner)