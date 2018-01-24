import json

dir1 = 'F:/jsonBus/bus-stop-data-by-id.json'
dir2 = 'F:/jsonBus/bus-stop-ids-of-lines.json'

outputfile1 = json.loads(open(dir1, encoding="utf-8").read())
outputfile2 = json.loads(open(dir2, encoding="utf-8").read())

def getTownShipList():
    townshipList = []
    for x in outputfile1:
        for y in outputfile1[x]:
            if y == 'township':
                townshipList.append(outputfile1[x][y])
    return townshipList



def searchBusInfo(township):
    busList = []
    for x in outputfile1:
        for y in outputfile1[x]:
            if y == 'township':
                if outputfile1[x][y] == township:
                    busList.append(x)
    return busList


def searchBusStop(busList):
    busStopList = []
    for x in outputfile2:
        for y in outputfile2[x]:
            for z in busList:
                if (z == y):
                    if checkIfexist(busStopList, x):
                        pass
                    else:
                        busStopList.append(x)
    return busStopList


def checkIfexist(dataList, dataInput):
    for x in dataList:
        if (x == dataInput):
            return True
    return False

townshipList = getTownShipList()
for township in townshipList:
    print(township)
    listToSearch = searchBusInfo(township)
    #print(listToSearch)
    #print(len(listToSearch))
    print(searchBusStop(listToSearch))
