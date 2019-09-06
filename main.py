


f=open("laura.xml")
lines=f.readlines()
ID="VTO_0039818"
CharacterNumber="UBERON_2000226"
checkDetail=False



def run(ID,CharacterNumber):
    global lines
    lineList=[]
    started=False
    for line in lines:
        if "row" in line.strip()[:7]:started=False
        if "row" in line.strip()[:7]:
            if ID in line:
                started= True
        
        if started:
            lineList.append(line)
    
    cellList=[]
    for line in lineList:
        if "cell" in line.strip()[:7]:started=False
        if "cell" in line.strip()[:7]:
            if CharacterNumber in line:
                started= True
        
        if started:
            cellList.append(line)
            

    CellLineOne=cellList[0]
    index=CellLineOne.find('>')
    present=CellLineOne[index-2]
    
    
    
    inferredPresent=False; #1 false
    assertedPresent=False; #1 true
    inferredAbsent=False;  #0 false
    assertedAbsent=False;  #0 true
    
    for i in range(0,len(cellList)):
        line=cellList[i]
        if (CharacterNumber+"_1") in line:
            presentLine=cellList[i+2]
            if "false" in presentLine:
                inferredPresent=True
            if "true" in presentLine:
                assertedPresent=True
        if (CharacterNumber+"_0") in line:
            presentLine=cellList[i+2]
            if "false" in presentLine:
                inferredAbsent=True
            if "true" in presentLine:
                assertedAbsent=True
    
    
    
    
    
    
    
    if checkDetail:
        for line in cellList:
            print line,
    f.close()
    print inferredPresent,assertedPresent,inferredAbsent,assertedAbsent
    return inferredPresent,assertedPresent,inferredAbsent,assertedAbsent

#run(ID,CharacterNumber)
        
