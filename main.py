from linkedList import LinkedList

mylist=LinkedList()

numbers=[0,1,2,3,4,5,6]
for number in numbers:
    mylist.add(number)

mylist.remove(6)

print(mylist)
