from math import ceil

bill = int(input("Enter bill"))
s = input("Satisafction level 0 for BAD, 5 for AVERAGE 10 for GREAT")
t = int

if  s == "0": 
    t = 0
elif s == "5":
    t = 15
elif s == "10":
    t  = 20


tip = ceil((t/100) * bill)
tbill = bill + tip

print(bill, tip, tbill)

