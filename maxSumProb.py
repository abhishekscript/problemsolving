

def main(dataA, dataB, num):
    
    result = []  
    
    setA = set(dataA)
    setB = set(dataB)

    def find(dataList, num, path=()):
        print(dataList, num, "path=", path)
        if not dataList:
            return
        if dataList[0] == num:
            print("stop cutting", dataList)
            result.append(path + (dataList[0],))
        else:
            find(dataList[1:], num - dataList[0], path + (dataList[0],))
            find(dataList[1:], num, path)
    
    data = list( setA.union(setB)  ) 
    find(data, num)
    
    
    # FIND IF NUMBER IS AVAILABLE IN BOTH
    finalData = []
    for x in result:
        availInBoth = {"setA" : False, "setB" : False }
        for y in x:
            if y in setA:
                availInBoth["setA"] = True
            if y in setB:
                availInBoth["setB"] = True

        if availInBoth["setA"] and availInBoth["setB"]:
            finalData.append(x)
    print(finalData)

dataA  = [10,2,8,1,9,5,2,3]
dataB  = [5,4,1,2,6,8,9,3,2,1]
target =15

if __name__=="__main__":
    main(dataA, dataB, target)