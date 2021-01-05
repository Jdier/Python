


with open('RawData_TabDelimitted.txt') as dataTabDelim:         
     content = dataTabDelim.readlines() 

with open('exportedParsedData.csv','w') as outputFile:
    outputFile.write('Campus,Department,Unit,Year,Month,Day\n')
    for strline in content:
        lineData = strline.split("\t")
        campusDept = lineData[0]
        createdTimestamp = lineData[1]
        
        campusDeptArray = campusDept.split("|")
        
        campus = campusDeptArray[0].strip()
     
        if (len(campusDeptArray) == 1):
            department = ""
            unit = ""
        elif (len(campusDeptArray) == 2):
            department = campusDeptArray[1].strip()
            unit=""
        else:
            department = campusDeptArray[1].strip()
            unit = campusDeptArray[2].strip()
        
        createdTimestampArray = createdTimestamp.split("-")
        strYear = createdTimestampArray[0]
        strMonth = createdTimestampArray[1]
        strDay = createdTimestampArray[2]
        strCorrectDay = strDay[0:2]
        
        
        outputFile.write("{},{},{},{},{},{}\n".format(campus,department,unit,strYear,strMonth,strCorrectDay))
        
        
        