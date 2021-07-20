def main():
    Dict1=dict()
    Dict2=dict()
    Dict3=dict()

    Dict1["Roll_No1"]=76.00
    Dict1["Roll_No2"]=45.00
    Dict1["Roll_No3"]=58.00


    Dict2["Roll_No1"]=65.00
    Dict2["Roll_No2"]=75.00
    Dict2["Roll_No3"]=65.00

    for keys in Dict1:
        Dict3[keys]=(Dict1[keys]+Dict2[keys])/2
    
    for x,y in Dict3.items():
        print(x,":",y)


if __name__=="__main__":
   main()           #calling main function
