def RemoveList(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
    return list2

def InputList():
    list1 = []
    n = int(input("Enter the number of element in list :"))
    for i in range(0, n):
        ele = int(input("Enter element :"))
        list1.append(ele)
    return list1

#Driver Code
lst1 = InputList()
RemoveList(lst1)
