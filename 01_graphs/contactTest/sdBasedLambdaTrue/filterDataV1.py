#!/usr/bin/python

flNm = "totalForce_4Ref3"
# ~ flNm = "totalForce_8Ref2"
# ~ flNm = "totalForce_16Ref1"
# ~ flNm = "totalForce_32NoRef"
filterFreq = 5

with open(flNm, 'r') as file:
            data = file.readlines()
            
filteredData = data[::filterFreq]

with open(flNm + "Filtered_%02d"%(filterFreq),'w') as file:
    file.writelines(filteredData)

