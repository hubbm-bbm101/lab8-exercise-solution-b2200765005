import sys


file = open(sys.argv[1],"r").read().split("\n")

dictFor={}
c=1
for i in file:
    splited=i.split(":")
    dictFor[splited[0]]=splited[1]
    c+=1


print(dictFor)


for i in sys.argv[2].split(","):
    try:
        print(f"{i},University: {dictFor[i]}")
    except:
        print(f"No Record '{i}' was found")

