input_string = input("Enter a list of numbers or elements separated by space: ")
n = input_string.split()
for num in n:
    if int(num)>=0:
        print(int(num))
    

