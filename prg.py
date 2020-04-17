n=input("1.Assigning elements to list\n2.Accessing elements from a tuple\n3.Deleting different dictiony elements\n4.Exit\n")
if n==1:
    list=[]
    print('enterting elements to a list. Type done to stop')
    while True:

        ele=input('enter element: ')
        done='done'
        if ele == done:
            break
        list.append(ele)
    print('Elements of the list:')
    print(list)
elif n==2:
    tup=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    m=input("enter the position of the element you want to access: ")
    print(tup[m])

elif n==3:
    d=dict()
    d={1:2 ,2:3 ,3:4 ,5:4 ,7:2}
    print('Dictionary elements:')
    print(d)
    ip=input('enter the key value of the element to be deleted: ')
    d.pop(ip)
    print('Dictionary after deleting the element:')
    print(d)

else:
    exit
