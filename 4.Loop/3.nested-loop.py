for i in range(1,4):
    for j in range(1,11):
        print(j)
    print()



'''Make this pattern:
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end ="  ")
    print()