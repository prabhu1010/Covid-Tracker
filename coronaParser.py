import sys
import numpy as np 

inFile = sys.argv[1]
dateList = []
dnc1 = []
dnc2 = []
dnc3 = []

def IsDecreasingList(l):
    print(l)
    idx = 1
    while idx < len(l):
        if l[idx] > l[idx-1]:
            return 0
        idx = idx + 1
    return 1

def GetDaysToGo(lst, tgt):
    d = round((tgt-lst[-1]) * (len(lst)-1)/(lst[-1] - lst[0]), 0)
    return d

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 
	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 
	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 
	# calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 
	return(b_0, b_1) 

def PrepareLists(inFile):
    found_val = 0
    fp = open(inFile, "r")
    for line in fp:
        rec = line.strip().upper()

        if "DAILY NEW CASES" in rec:
            found_val = 1 

        if "CATEGORIES:" in rec and found_val == 1:
            dateList = rec.split("[")[1].split("]")[0].split(",")

        if "DATA:" in rec and found_val == 1:
            dncList = rec.split("[")[1].split("]")[0].split(",")
            for n in dncList:
                try:
                    val = int(n) 
                    dnc1.append(val)
                except:
                    dnc1.append(n)
            #print(dateList, len(dateList))
            #print(dnc1, len(dnc1))
            if len(dnc1) != len(dateList):
                print("This shit is messed up - datecount not matching value count")
            break
    return dnc1, dateList

def GetPeaks(nList, dList):
    #print("Get Peaks")
    #print(nList)
    #print(dList)
    n = len(nList)
    #print(n)
    idx = 0
    while n - idx >= 5:   
        try:
            n1 = (float(nList[idx]) + nList[idx + 1] + nList[idx + 2] + nList[idx + 3] + nList[idx + 4]) / 5
            #print(nList[idx:idx+5])
            #print("adding", round(n1,2))
            dnc2.append(round(n1,2))
        except:
            x = 1
        idx = idx + 1
    #print(dnc2)

    n2 = len(dnc2)
    idx = 0
    while n2 - idx >= 5:   
        n1 = (float(dnc2[idx]) + dnc2[idx + 1] + dnc2[idx + 2] + dnc2[idx + 3] + dnc2[idx + 4] )/ 5
        #print(dnc2[idx:idx+5])
        idx = idx + 1
        #print("adding", round(n1,2))
        dnc3.append(round(n1,2))
    #print(" ")
    #print(dnc3)
    #print(" ")
    peakidx = dnc3.index(max(dnc3))
    #print("Found at index", peakidx) 
    dateidx = len(dnc3) - peakidx
    regressX = dnc3[peakidx:len(dnc3)]
    #print(regressX)
    regressY = list(range(1,(len(dnc3) - peakidx)+1))
    #print(regressY)
    return regressX, regressY, dateidx

print(" ")
dnc1, dateList = PrepareLists(inFile)
regX, regY,dateidx = GetPeaks(dnc1, dateList)
#print(regX)
#print(regY)
target = 500
days_to_go = int(GetDaysToGo(regX, target))
#print(days_to_go)

print(regX)
print(sys.argv[1], ": Last data is from", dateList[-1],"-", regX[-1],"Peak value is", max(dnc3),"which occured on", dateList[-dateidx],"; Days remaining to drop to",target,"cases is", days_to_go)
print(" ")

''' #USE THIS ONLY IF DATA IS ON A CONSISTENTLY ONE-WAY FALLING PATTERN
cluster_lengths = [7,14,21,28]
for i in cluster_lengths:
    tmplist = regX[-i:]
    tmplist.reverse()
    print(tmplist)
    if IsDecreasingList(tmplist):
        print("yes")
        print(regX[0], regX[-1], regX[0]-regX[-1],i) 
'''
