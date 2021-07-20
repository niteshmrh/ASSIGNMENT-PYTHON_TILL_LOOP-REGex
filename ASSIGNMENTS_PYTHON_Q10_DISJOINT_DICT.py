def main():
    myDict={"Sharp":"smart", #defining my dictionary
      "Bright":"student",
      "clever":"fox",
      "Dumb":"stupid"
      }

    myDict2={"fool":"stupid",
      "joy":"happy",
      "Sharp":"smart",
      "Dumb":"stupid"}

    disjoint_pairs = dict()
    for key in myDict:
       if (key not in myDict2):
           disjoint_pairs[key]=myDict[key]
    
    for key in myDict2:
       if (key not in myDict):
           disjoint_pairs[key]=myDict2[key]
    
    for x,y in disjoint_pairs.items():
        print(x,":",y)


if __name__=="__main__":
   main()               #calling main function
