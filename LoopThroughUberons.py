import main

ID="VTO_0041925"
familyID="VTO_0041850"
genusID="VTO_0041917"
f=open("entities_UberonID.csv")
lines=f.readlines()

UBList=[]

NameList=[]
AssertList=[]
InferredList=[]
familyList=[]
genusList=[]


for line in lines:
    try:
        splitList=line.split(",")
        UBraw=splitList[0]
        name=splitList[1]
        name=name.replace('"','').strip()
        
        UB=UBraw.split("/")[4]
        UB=UB.replace('"','').strip()
        
        
        inferredPresent,assertPresent,inferredAbsent,assertAbsent=main.run(ID,UB)

        if inferredPresent and inferredAbsent:
            InferredList.append("0 and 1")
        elif inferredPresent and not inferredAbsent:
            InferredList.append("1")
        elif not inferredPresent and inferredAbsent:
            InferredList.append("0")
        else:
            InferredList.append("")
            
        if assertPresent and assertAbsent:
            AssertList.append("0 and 1")
        elif assertPresent and not assertAbsent:
            AssertList.append("1")
        elif not assertPresent and assertAbsent:
            AssertList.append("0")
        else:
            AssertList.append("")
        NameList.append(name)       
        
    except:
        NameList.append(name)
        AssertList.append("")
        InferredList.append("")
        continue


ID=familyID
for line in lines:
    try:
        splitList=line.split(",")
        UBraw=splitList[0]
        UB=UBraw.split("/")[4]
        UB=UB.replace('"','').strip()
        inferredPresent,assertPresent,inferredAbsent,assertAbsent=main.run(ID,UB)
        present=False
	absent=False 
	if inferredPresent or assertPresent:
            present=True
        if inferredAbsent or assertAbsent:
            absent=True      
        if present and absent:
           familyList.append("0 and 1")
        elif present:
           familyList.append("1")
        elif absent:
           familyList.append("0")
        else: 
           familyList.append("")
            
    except:
        familyList.append("")
        continue

ID=genusID
for line in lines:
    try:
	print "genus"
        splitList=line.split(",")
        UBraw=splitList[0]
        UB=UBraw.split("/")[4]
        UB=UB.replace('"','').strip()
        inferredPresent,assertPresent,inferredAbsent,assertAbsent=main.run(ID,UB)
        present=False
	absent=False 
	if inferredPresent or assertPresent:
            present=True
        if inferredAbsent or assertAbsent:
            absent=True      
        if present and absent:
           genusList.append("0 and 1")
        elif present:
           genusList.append("1")
        elif absent:
           genusList.append("0")
        else: 
           genusList.append("")
    
    except:
        genusList.append("")
        continue



outputString=""
outputString+='Result based On %s \n'%familyID
outputString+=",Asserted"+",Inferred"+",Family"+",Genus"+"\n"
for i in range(len(NameList)):
    line= NameList[i]+","+AssertList[i]+","+InferredList[i]+","+familyList[i]+","+genusList[i]+"\n"
    outputString+=line

f=open("output.csv","w")
f.write(outputString)
f.close()
print "Finished!"



