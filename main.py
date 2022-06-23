alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
speChar = ["!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~",".", "’"]
speStr = []
finList2 = []
speInd = []
cipherFile = open("codecipher.txt", "r")
evenorodd = 0
cipherNum = 0
wordStr = ""
appendList= []
for line in cipherFile.readlines():
  evenorodd+=1
  if evenorodd == 1:
    cipherNum = line
  if evenorodd ==2:
    evenorodd=0
    for word in line:
      for letter in word:
        if not letter.isalpha():
          wordStr = str(wordStr) + str(letter)
          continue
        for alphaletter in alphabet:
          if letter == alphaletter:
            ez=alphabet.index(alphaletter)
            if int(ez)+int(cipherNum) > 25:
              fe=(int(ez)+int(cipherNum))-26;wordStr = str(wordStr) + str(alphabet[fe])
            else:
              ez=int(ez)+int(cipherNum);wordStr = str(wordStr) + str(alphabet[ez])
    appendList.append(wordStr)
    wordStr=""
counter = 0
counter2 = 0
finList = []
specList = []
for i in appendList:
  e = appendList[counter]
  yesList = e.split(" ")
  for j in yesList:
    f = j.replace("\n", "")
    g = list(f)
    for spe in g:
      for l in speChar:
        if spe == l:
          cd = g.index(spe)
          speInd.append((appendList.index(i),yesList.index(j),cd))
          speStr.append(g[cd])
          g.pop(cd)
    lenStr=len(g)
    revStr=g[lenStr::-1]
    for ol in speInd:
      if appendList.index(i) == ol[0] and yesList.index(j) == ol[1]:
        revStr.insert(ol[2],speStr[speInd.index(ol)])
    finList.append(revStr)
  counter+=1
cipherFile.close()
for p in finList:
  finList2.append("".join(p))
print(finList2)
cipherOut = open("cipherOut.txt", "a")
for t in finList2:
  cipherOut.write(t + " ")
cipherOut.close()