
invlist = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
secondlist = ["iron", "iron", "coal", "coal", "wood", "wood", "diamond", "diamond"]
decrementlist = ["diamond", "coal", "iron", "iron"]
invDict = {}
oneDict = {}
secondDict = {}
mnDict ={}

def createInventory(invlist):
    invDict = {}
    def dictcreate(list, word):
        count = 0
        for i in list:
            if i == word: 
                count = count + 1 
        return count 

    for i in invlist:
        value = dictcreate(invlist, i)
        invDict[i] = value

    print('invDict',invDict)

def createInventorywithReturn(invlist):
    invDict = {}
    def dictcreate(list, word):
        count = 0
        for i in list:
            if i == word: 
                count = count + 1 
        return count 

    for i in invlist:
        value = dictcreate(invlist, i)
        invDict[i] = value

    print('invDict',invDict)
    return invDict



def decrementList(invlist,decrementlist):
    newinvList = invlist
    oneDict = {}
    def removeitem(List, item):
        for i in invlist:
            if i == item:
                List.remove(i)
                break
        return List

    def createinv(invlist, Dict):
        def dictcreate(list, word):
            count = 0
            for i in list:
                if i == word: 
                    count = count + 1 
            return count 

        for i in invlist:
            value = dictcreate(invlist, i)
            Dict[i] = value
        print('Dict',Dict)
        return Dict

    for i in decrementlist:
        newinvList = removeitem(newinvList, i)
    
    oneDict = createinv(invlist,oneDict)
    print('oneDict',oneDict)
    return oneDict

def compareDict(first,second):
    def getItem(keyvalue):
        if keyvalue in second:  
            print('second',keyvalue)
        else:
            first[keyvalue] = 0

    for key, value in first.items():
            print(key,value)
            strkey = getItem(key)
    return first

def deleteKey(dict, key):
    if key in dict:
        del dict[key]
    return dict

def getTuple(dict):
    tup = ()
    for key in dict:
        if dict[key] > 0:
            str = key , dict[key] 
            tup = tup + (str,)
    return tup


createInventory(invlist)
invlist.extend(secondlist)
print('secondlist',invlist)
createInventory(invlist)
mnDict = createInventorywithReturn(invlist)
print('createInventory',invlist)
oneDict = decrementList(invlist,decrementlist)
print('decrementList',invlist)
createInventory(invlist)
print('createInventory',invlist)
mnDict = compareDict(mnDict,oneDict)
deleteKey(oneDict,'coal')
print('mnDict',mnDict, 'oneDict', oneDict)
tup = getTuple(mnDict)
print('tup',tup)


