def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
          for j in range(0,k):
              print(end=" ")
          k = k - 1
          for j in range(0, i+1):
              print("*", end=" ")
          print("\n")

def primeNumber(n):
    list1 = []
    start = 1
    end = n*10
    for i in range(start, end):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                # print(i)
                list1.append(i)
    return list1

# Driver code
column = int(input("Enter the number of column :")) 
lst = primeNumber(column)
print(lst)
pattern(column)

